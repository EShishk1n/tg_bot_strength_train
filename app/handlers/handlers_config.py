def is_right_exercise_format(exercise: str) -> bool:
    try:
        weight, repetitions, sets, quantity = exercise.split('*')
        if is_right_format(weight) and is_right_format(repetitions) and is_right_format(sets) and is_right_format(
                quantity):
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
