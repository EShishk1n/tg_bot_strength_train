from app.database.models import Purpose, WorkingWeight
from app.services.calculate_workout_program.exercise_class import Exercise, PurposeExercise


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
