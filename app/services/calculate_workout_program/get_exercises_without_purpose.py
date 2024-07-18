from app.database.models import Purpose


def get_exercises_without_purpose(purpose: Purpose) -> list:
    exercises_without_purpose = []
    purpose = purpose[0]
    for attr in dir(purpose):
        if not attr.startswith(('__', '_')):
            if getattr(purpose, attr) is None:
                if attr not in ('date_reached_at_actually', 'date_reached_at_plan', 'desired_result', 'id', ):
                    exercises_without_purpose.append(str(attr))
    return exercises_without_purpose


def get_exercises_with_purpose(purpose: Purpose) -> list:
    all_exercises = ['deadlift', 'squatting', 'bench_press', 'standing_barbell_curl', 'pull_up',
                     'dumbbell_incline_bench_press', 'military_press', 'lat_pull_down',
                     'seated_row']
    exercises_with_purpose = []
    exercises_without_purpose = get_exercises_without_purpose(purpose)
    for exercise in all_exercises:
        if exercise not in exercises_without_purpose:
            exercises_with_purpose.append(exercise)

    return exercises_with_purpose
