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
    if some_string.isdigit() and len(some_string) <= 3:
        return True
    else:
        return False
