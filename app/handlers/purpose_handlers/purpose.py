from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.purpose_keyboard import purpose_keyboard

router = Router(name='purpose')


@router.callback_query(F.data == 'purpose')
async def purpose(callback: CallbackQuery):
    await callback.message.edit_text('Вы перешли в блок "Цель тренировок"',
                                     reply_markup=purpose_keyboard)


@router.callback_query(F.data == 'get_back_to_purpose_menu')
async def get_back_to_purpose_menu(callback: CallbackQuery):
    await callback.message.edit_text('Вы перешли в блок "Цель тренировок"\n'
                                     'Выберите пункт:', reply_markup=purpose_keyboard)
