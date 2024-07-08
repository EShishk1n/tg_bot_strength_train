from aiogram.fsm.state import StatesGroup, State


class PurposeExercise(StatesGroup):
    exercise_name = State()
    exercise_purpose = State()


class DesiredResult(StatesGroup):
    desired_result = State()
