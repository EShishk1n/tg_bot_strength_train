from aiogram import F, Router
from aiogram.types import CallbackQuery, FSInputFile

from app.handlers.workout_handlers.workout_info.make_xlsx_file import create_file_with_all_workouts_info
from app.keyboards.workout_keyboard import get_back_to_workout_info_keyboard

router = Router(name='all_workouts_info')


@router.callback_query(F.data == 'all_workouts_info')
async def all_workouts_info(callback: CallbackQuery):
    await callback.answer('')
    filename = await create_file_with_all_workouts_info()
    input_file = FSInputFile(filename)
    await callback.message.edit_text('Информация о всех тренировках в файле ниже.',
                                     reply_markup=get_back_to_workout_info_keyboard)
    await callback.message.reply_document(document=input_file)
