from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery

from app.database.queries import ORMPurpose
from app.keyboards.workout_keyboard import workout_keyboard

router = Router(name='workout')


@router.callback_query(F.data == 'workout')
async def workout(callback: CallbackQuery):
    if await ORMPurpose.is_user_has_purpose(callback.from_user.id):
        await callback.message.edit_text('Вы перешли в блок "Тренировка"',
                                         reply_markup=workout_keyboard)
    else:
        await callback.message.edit_text('Вы перешли в блок "Тренировка"\n'
                                         f'Вернитесь в основное меню, выберите пункт "Цель тренировок", "Задать цель"',
                                         reply_markup=workout_keyboard)


@router.callback_query(F.data == 'get_back_to_workout_menu')
async def get_back_to_workout_menu(callback: CallbackQuery):
    try:
        await callback.message.edit_text('Вы перешли в блок "Тренировка"\n'
                                         'Выберите пункт:', reply_markup=workout_keyboard)
    except TelegramBadRequest:
        await callback.message.answer('Вы перешли в блок "Тренировка"\n'
                                      'Выберите пункт:', reply_markup=workout_keyboard)
