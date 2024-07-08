from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from app.keyboards.user_keyboard import user_keyboard

router = Router(name='user')


@router.callback_query(F.data == 'user')
async def user(callback: CallbackQuery):
    await callback.message.edit_text('Вы перешли в блок "Пользователь"\n'
                                     'Выберите пункт:', reply_markup=user_keyboard)


@router.callback_query(F.data == 'get_back_to_user_menu')
async def get_back_to_user_menu(callback: CallbackQuery):
    await callback.message.edit_text('Вы перешли в блок "Пользователь"\n'
                                     'Выберите пункт:', reply_markup=user_keyboard)
