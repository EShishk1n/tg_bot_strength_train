from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.database.queries import ORMUser
from app.keyboards.user_keyboard import get_back_to_user_menu_keyboard

router = Router(name='user_info')


@router.callback_query(F.data == 'user_info')
async def user_info_(callback: CallbackQuery):
    await callback.answer('')
    if await ORMUser.is_user_registered(callback.from_user.id):
        user_info = await ORMUser.get_user_info(callback.from_user.id)
        await callback.message.edit_text(f'Информация о пользователе {user_info[0].name}\n'
                                         f' - возраст: {user_info[0].age}\n'
                                         f' - вес: {user_info[0].weight}\n'
                                         f' - рост: {user_info[0].height}\n'
                                         f' - продолжительность тренировок: {user_info[0].duration_of_const_train}\n'
                                         f' - аккаунт создан: {user_info[0].created_at.date().strftime("%d.%m.%Y")}',
                                         reply_markup=get_back_to_user_menu_keyboard)
    else:
        await callback.message.edit_text(f'Мы не знакомы(\n'
                                         f'Предлагаю пройти регистрацию',
                                         reply_markup=get_back_to_user_menu_keyboard)
