def is_right_purpose_exercise_format(exercise: str) -> bool:
    try:
        weight, repetitions, sets, quantity = exercise.split('*')
        if is_right_format(weight) and is_right_format(repetitions) and is_right_format(sets) and is_right_format(
                quantity):
            return True
        else:
            return False
    except ValueError:
        return False


def is_right_exercise_format(exercise: str) -> bool:
    try:
        weight, repetitions, sets = exercise.split('*')
        if is_right_format(weight) and is_right_format(repetitions) and is_right_format(sets):
            return True
        else:
            return False
    except ValueError:
        return False


def is_right_format(some_string: str) -> bool:
    try:
        float(some_string)
        if len(some_string) <= 4:
            return True
        else:
            return False
    except ValueError:
        return False


def is_date_format(some_string: str) -> bool:
    day, month, year = some_string.split('.')
    if 0 < int(day) <= 31 and 0 < int(month) <= 12 and 0 < int(year) <= 2050 and (
            len(day) + len(month) + len(year)) == 8:
        return True
    else:
        return False


exercise_dict = {
    'deadlift': 'становая тяга',
    'squatting': 'приседания',
    'bench_press': 'жим лежа',
    'standing_barbell_curl': 'сгибание рук со штангой',
    'pull_up': 'подтягивания',
    'dumbbell_incline_bench_press': 'жим гантелей в наклоне',
    'military_press': 'жим штанги стоя',
    'lat_pull_down': 'тяга верхнего блока',
    'seated_row': 'тяга нижнего блока',
    'становая тяга': 'deadlift',
    'приседания': 'squatting',
    'жим лежа': 'bench_press',
    'сгибание рук со штангой': 'standing_barbell_curl',
    'подтягивания': 'pull_up',
    'жим гантелей в наклоне': 'dumbbell_incline_bench_press',
    'жим штанги стоя': 'military_press',
    'тяга верхнего блока': 'lat_pull_down',
    'тяга нижнего блока': 'seated_row',
}
