from app.database.models import Purpose


def get_exercises_without_purpose(purpose: Purpose) -> list:
    exercises_without_purpose = []
    for attr in dir(purpose):
        if not attr.startswith(('__', '_')):
            if getattr(purpose, attr) is None:
                if attr != 'date_reached_at_actually':
                    exercises_without_purpose.append(str(attr))
    return exercises_without_purpose


def get_exercises_with_purpose(purpose: Purpose) -> list:
    all_exercises = ['deadlift', 'sqatting', 'bench_press', 'barbell_curl', 'pull_up',
                     'dumbbell_inclene_bench_press', 'military_press', 'lat_pull_down',
                     'seated_row']
    exercises_with_purpose = []
    exercises_without_purpose = get_exercises_without_purpose(purpose)
    for exercise in all_exercises:
        if exercise not in exercises_without_purpose:
            exercises_with_purpose.append(exercise)

    return exercises_with_purpose
