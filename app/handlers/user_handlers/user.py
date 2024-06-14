from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router(name='user')


@router.callback_query(F.data == 'user')
async def user(callback: CallbackQuery):
    await callback.answer('Вы перешли в блок "Пользователь"')
    # await callback.message.answer(f'Введите цель для упражнения {exercise_name.upper()}\n'
    #                               f'Формат записи упражнения - ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')