from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.queries import ORMUser
from app.handlers.user_handlers.user import router
from app.handlers.user_handlers.user_states import Reg
from app.keyboards.user_keyboard import sex_keyboard, duration_of_const_train_keyboard


# Запускает регистрацию, ловит tg_id, переключает FSM на имя
@router.message(F.text == 'Начать регистрацию')
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.tg_id)
    await state.update_data(tg_id=message.from_user.id)
    await state.set_state(Reg.name)
    await message.answer('Напишите свое имя')


# Ловит имя, переключает FSM на возраст
@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.age)
    await message.answer('Напишите свой возраст')


# Ловит возраст, переключает FSM на пол
@router.message(Reg.age)
async def reg_three(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Reg.sex)
        await message.answer('Выберите пол', reply_markup=sex_keyboard)
    else:
        await message.answer('Зачем балуешься? Возраст записывается цифрами. Повтори ввод.')


# Ловит пол, переключает FSM на вес
@router.message(Reg.sex)
async def reg_four(message: Message, state: FSMContext):
    if message.text in ['Мужской', 'Женский']:
        await state.update_data(sex=message.text)
        await state.set_state(Reg.weight)
        await message.answer('Напишите свой вес. Чем точнее данные, '
                             'тем корректнее будет составлена программа тренировок')
    else:
        await message.answer('Существует только два гендера. Выбери вариант с клавиатуры')


# Ловит вес, переключает FSM на рост
@router.message(Reg.weight)
async def reg_five(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        await state.set_state(Reg.height)
        await message.answer('Напишите свой рост')
    else:
        await message.answer('Не балуйся! Вес записывается цифрами. Повтори ввод.')


# Ловит рост, переключает FSM на опыт тренировок
@router.message(Reg.height)
async def reg_six(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(height=message.text)
        await state.set_state(Reg.duration_of_const_train)
        await message.answer('Выберите опыт постоянных тренировок (перерывы между тренировками не более 2 месяцев)',
                             reply_markup=duration_of_const_train_keyboard)
    else:
        await message.answer('Не балуйся! Рост записывается цифрами. Повтори ввод.')


# Ловит опыт тренировок, закрывает FSM, записывает данные в БД
@router.message(Reg.duration_of_const_train)
async def reg_seven(message: Message, state: FSMContext):
    if message.text in ['только начинаю', 'более 3 месяцев', 'более года', 'более 3 лет']:
        await state.update_data(duration_of_const_train=message.text)
        data = await state.get_data()
        await state.clear()
        await ORMUser.reg_user(user_data=data)
        await message.answer('Аккаунт успешно создан!')
    else:
        await message.answer('Нужно выбрать значение на клавиатуре, иначе обновить информацию не получится.')
