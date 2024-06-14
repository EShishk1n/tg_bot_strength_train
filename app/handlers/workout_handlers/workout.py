from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router(name='workout')


@router.callback_query(F.data == 'workout')
async def purpose(callback: CallbackQuery):
    await callback.answer('Вы перешли в блок "Тренировка"')
    # await callback.message.answer(f'Введите цель для упражнения {exercise_name.upper()}\n'
    #                               f'Формат записи упражнения - ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')