import asyncio

from app.database.models import Purpose, WorkingWeight
from app.database.queries import ORMPurpose, ORMWorkingWeight
from app.services.class_for_calculation_workout_program import WorkoutProgramCalculation
from app.services.exercise_class import Exercise, PurposeExercise


async def pick_data_for_calculation_workout_program(purpose: Purpose, working_weight: WorkingWeight,
                                                    exercise: str) -> dict:
    purpose_exercise = str(purpose.__getattribute__(exercise))
    current_exercise = (f'{working_weight.__getattribute__(exercise)}*'
                        f'{purpose_exercise.split("*")[1]}*'
                        f'{purpose_exercise.split("*")[2]}')
    date_reached_at_plan = purpose.__getattribute__('date_reached_at_plan')
    desired_result = str(purpose.__getattribute__('desired_result'))

    res = {'current_exercise': Exercise(current_exercise),
           'purpose_exercise': PurposeExercise(purpose_exercise),
           'date_reached_at_plan': date_reached_at_plan,
           'desired_result': desired_result}

    return res


async def main():
    user_id = 134482654
    purpose = await ORMPurpose.get_purpose(user_id)
    working_weight = await ORMWorkingWeight.get_working_weight(user_id)
    exercise = 'military_press'
    data = await pick_data_for_calculation_workout_program(purpose[0], working_weight[0], exercise)
    workout_program = WorkoutProgramCalculation(current_exercise=data['current_exercise'],
                                                purpose_exercise=data['purpose_exercise'],
                                                date_reached_at_plan=data['date_reached_at_plan'],
                                                desired_result=data['desired_result'])

    print(workout_program.calculate_workout_program())


if __name__ == "__main__":
    asyncio.run(main())
