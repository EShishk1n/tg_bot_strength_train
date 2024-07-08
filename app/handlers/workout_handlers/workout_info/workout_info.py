from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.keyboards.workout_keyboard import workout_info_keyboard

router = Router(name='workout_info')


@router.callback_query(F.data == 'workout_info')
async def workout_info(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        'В каком виде вы хотите получить информацию?\n', reply_markup=workout_info_keyboard)


@router.callback_query(F.data == 'get_back_to_workout_info_menu')
async def get_back_to_workout_info_menu(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text(
        'В каком виде вы хотите получить информацию?\n', reply_markup=workout_info_keyboard)
