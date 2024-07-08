from aiogram.fsm.state import StatesGroup, State


class Reg(StatesGroup):
    tg_id = State()
    name = State()
    age = State()
    sex = State()
    weight = State()
    height = State()


class UpdateAge(StatesGroup):
    age = State()


class UpdateWeight(StatesGroup):
    weight = State()
