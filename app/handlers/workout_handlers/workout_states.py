from aiogram.fsm.state import StatesGroup, State


class WorkoutExercise(StatesGroup):
    exercise_name = State()
    exercise_workout = State()
