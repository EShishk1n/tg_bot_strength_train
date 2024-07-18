import asyncio

from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile

from app.keyboards.workout_keyboard import get_back_to_workout_menu_keyboard
from app.services.make_xlsx_file.make_xlsx_file import create_file_with_all_workouts_info
from run import bot

router = Router(name='workout_info')


@router.callback_query(F.data == 'workout_info')
async def workout_info(callback: CallbackQuery):
    await callback.answer('')
    filename = await create_file_with_all_workouts_info(callback.from_user.id)
    input_file = FSInputFile(filename)
    await callback.message.edit_text(
        'Информация о всех тренировках в файле ниже. Скачайте файл, через 15 секунд он удалится.',
        reply_markup=get_back_to_workout_menu_keyboard)
    chat_id = callback.message.chat.id
    file = await bot.send_document(chat_id=chat_id,
                                   document=input_file)
    await asyncio.sleep(15)
    await bot.delete_message(chat_id=chat_id, message_id=file.message_id)
