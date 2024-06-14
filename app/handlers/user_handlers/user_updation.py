from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.database.queries import ORMUser
from app.handlers.user_handlers.user import router
from app.handlers.user_handlers.user_states import Update
from app.keyboards.user_keyboard import duration_of_const_train_keyboard


# Запускает обновление информации, переключает FSM на возраст
@router.message(F.text == 'Обновить данные')
async def update_one(message: Message, state: FSMContext):
    await state.set_state(Update.age)
    await message.answer('Напишите свой возраст')


# Ловит возраст, переключает FSM на вес
@router.message(Update.age)
async def update_two(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Update.weight)
        await message.answer('Напишите свой вес. Чем точнее данные, '
                             'тем корректнее будет составлена программа тренировок')
    else:
        await message.answer('Зачем балуешься? Возраст записывается цифрами. Повтори ввод.')


# Ловит вес, переключает FSM на опыт тренировок
@router.message(Update.weight)
async def update_three(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(weight=message.text)
        await state.set_state(Update.height)
        await message.answer('Выберите опыт постоянных тренировок (перерывы между тренировками не более 2 месяцев)',
                             reply_markup=duration_of_const_train_keyboard)
    else:
        await message.answer('Не балуйся! Вес записывается цифрами. Повтори ввод.')


# Ловит опыт тренировок, закрывает FSM, записывает данные в БД
@router.message(Update.duration_of_const_train)
async def update_four(message: Message, state: FSMContext):
    if message.text in ['только начинаю', 'более 3 месяцев', 'более года', 'более 3 лет']:
        await state.update_data(duration_of_const_train=message.text)
        data = await state.get_data()
        tg_id = message.from_user.id
        await ORMUser.update_user(tg_id=tg_id, user_data=data)
        await message.answer('Информация успешно обновлена!')
    else:
        await message.answer('Нужно выбрать значение на клавиатуре, иначе обновить информацию не получится.')
