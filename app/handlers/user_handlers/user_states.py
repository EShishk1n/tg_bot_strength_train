from aiogram.fsm.state import StatesGroup, State


class Reg(StatesGroup):
    tg_id = State()
    name = State()
    age = State()
    sex = State()
    weight = State()
    height = State()
    duration_of_const_train = State()


class Update(StatesGroup):
    age = State()
    weight = State()
    height = State()
    duration_of_const_train = State()
