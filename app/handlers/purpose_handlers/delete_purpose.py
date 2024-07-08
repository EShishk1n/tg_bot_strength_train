from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.database.queries import ORMPurpose
from app.keyboards.purpose_keyboard import purpose_keyboard

router = Router(name='delete_purpose')


@router.callback_query(F.data == 'delete_purpose')
async def delete_purpose(callback: CallbackQuery):
    await ORMPurpose.delete_purpose(callback.from_user.id)
    await callback.message.edit_text('Цель удалена',
                                     reply_markup=purpose_keyboard)
