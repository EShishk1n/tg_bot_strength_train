from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.keyboards.purpose_keyboard import get_back_to_purpose_menu_keyboard
from app.database.queries import ORMPurpose

from app.keyboards.purpose_keyboard import exercise_keyboard

router = Router(name='update_purpose')


# Ловит команду /update_purpose
@router.callback_query(F.data == 'update_purpose')
async def update_purpose(callback: CallbackQuery):
    if await ORMPurpose.is_user_has_purpose(callback.from_user.id):
        await callback.message.edit_text('Выбери упражнение для обновления цели',
                                         reply_markup=exercise_keyboard)
    else:
        await callback.message.edit_text(f'Цель не задана.\n'
                                         f'Вернитесь в меню "Цель тренировок" и выберите пунки "Задать цель"',
                                         reply_markup=get_back_to_purpose_menu_keyboard)

# Дальше работает по хэндлерам из create_purpose
