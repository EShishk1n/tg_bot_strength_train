from datetime import datetime, timedelta

from app.services.exercise_class import Exercise, PurposeExercise


def main(current_exercise: Exercise, purpose_exercise: PurposeExercise, date_reached_at_plan: datetime.date):
    start_weight = current_exercise.calculate_current_exercise_weight()
    purpose_weight = purpose_exercise.calculate_current_exercise_weight()
    weeks_quantity_for_reach_purpose = calculate_weeks_quantity_for_reach_purpose(date_reached_at_plan)
    exercise_quantity_for_reach_purpose = calculate_exercise_quantity_for_reach_purpose(
        weeks_quantity_for_reach_purpose, exercice_frequency=purpose_exercise.frequency)
    step_of_exercise_weight = calculate_step_of_exercise_weight(start_weight, purpose_weight,
                                                                exercise_quantity_for_reach_purpose)

    return create_list_of_exercise_weight(start_weight, exercise_quantity_for_reach_purpose, step_of_exercise_weight)


def create_list_of_exercise_weight(start_weight: float, exercise_quantity_for_reached_purpose: int,
                                   step: float) -> list[float]:
    """Создает список суммарных весов упражнения от стартового показателя до целевого"""

    list_of_exercise_weight = [start_weight]
    for _ in range(1, exercise_quantity_for_reached_purpose):
        list_of_exercise_weight.append(start_weight + step * _)

    return list_of_exercise_weight


def calculate_weeks_quantity_for_reach_purpose(date_reached_at_plan: datetime.date) -> int:
    """Считает количество недель до плановой даты достижения цели"""

    today = datetime.now().date()
    days_quantity_for_reach_purpose = (date_reached_at_plan.date() - today).days
    weeks_quantity_for_reach_purpose = int(days_quantity_for_reach_purpose / 7)

    return weeks_quantity_for_reach_purpose


def calculate_step_of_exercise_weight(start_weight: float, purpose_weight: float,
                                      exercise_quantity_for_reached_purpose: int) -> float:
    """Считает насколько должен увеличиватсья суммарный вес упражнения"""

    return (purpose_weight - start_weight) / (exercise_quantity_for_reached_purpose - 1)


def calculate_exercise_quantity_for_reach_purpose(weeks_quantity_for_reach_purpose: int,
                                                  exercice_frequency: int) -> int:
    """Считает количество упражнений за весь период"""

    return weeks_quantity_for_reach_purpose * exercice_frequency

