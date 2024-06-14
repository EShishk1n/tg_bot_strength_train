from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router(name='purpose')


@router.callback_query(F.data == 'purpose')
async def purpose(callback: CallbackQuery):
    await callback.answer('Вы перешли в блок "Цель тренировок"')
    # await callback.message.answer(f'Введите цель для упражнения {exercise_name.upper()}\n'
    #                               f'Формат записи упражнения - ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')