from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.database.queries import ORMUser
from app.handlers.user_handlers.user_states import UpdateAge, UpdateWeight
from app.keyboards.user_keyboard import get_back_to_user_menu_keyboard, \
    params_for_updating_keyboard

router = Router(name='user_updation')


@router.callback_query(F.data == 'user_updation')
async def update_start(callback: CallbackQuery):
    await callback.answer('')
    if await ORMUser.is_user_registered(callback.from_user.id):
        await callback.message.edit_text('Выберите поле для обновления', reply_markup=params_for_updating_keyboard)
    else:
        await callback.message.edit_text('Сперва зарегистрируйтесь.', reply_markup=get_back_to_user_menu_keyboard)


# Запускает обновление возраста
@router.callback_query(F.data == 'update_age')
async def update_age(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(UpdateAge.age)
    await callback.message.answer('Напишите свой возраст')


# Ловит возраст, записывает данные
@router.message(UpdateAge.age)
async def update_age_two(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=int(message.text))
        data = await state.get_data()
        await state.clear()
        await ORMUser.update_user(tg_id=message.from_user.id, user_data=data)
        await message.answer('Возраст успешно обновлен.\nВыберите поле для обновления',
                             reply_markup=params_for_updating_keyboard)
    else:
        await message.answer('Не балуйся! Вес записывается цифрами. Повтори ввод.')


# Запускает обновление веса
@router.callback_query(F.data == 'update_weight')
async def update_weight(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(UpdateWeight.weight)
    await callback.message.answer('Напишите свой вес. Чем точнее данные, '
                                  'тем корректнее будет составлена программа тренировок')


# Ловит вес, записывает данные
@router.message(UpdateWeight.weight)
async def update_weight_two(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(weight=int(message.text))
        data = await state.get_data()
        await state.clear()
        await ORMUser.update_user(tg_id=message.from_user.id, user_data=data)
        await message.answer('Вес успешно обновлен\nВыберите поле для обновления',
                             reply_markup=params_for_updating_keyboard)
    else:
        await message.answer('Не балуйся! Вес записывается цифрами. Повтори ввод.')
