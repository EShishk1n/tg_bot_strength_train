from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from app.database.queries import ORMUser, ORMPurpose
from app.keyboards.main_keyboard import main_keyboard
from app.keyboards.purpose_keyboard import exercise_keyboard


router = Router(name='main_handlers')


# Ловит команду /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    if await ORMUser.is_user_registered(message.from_user.id):
        name = await ORMUser.get_username(message.from_user.id)
        await message.answer(f'С возвращением, {name}!\n'
                             f'Для продолжения тренировок предлагаю проверить актуальность информации в блоке '
                             f'"Пользователь" и "Цель тренировок"',
                             reply_markup=main_keyboard)
    else:
        await message.answer(
            f'Привет!\nЭто бот для контроля силовых тренировок.\n'
            f'Для начала тренировок зарегистрируйся и поставь цель в блоках ниже',
            reply_markup=main_keyboard)


# # Ловит команду /help
# @router.message(Command('help'))
# async def cmd_help(message: Message):
#     await message.answer('Это бот для контроля силовых тренировок.\n'
#                          'Основные команды:\n'
#                          '/purpose - вывести текущую цель тренировок,\n'
#                          '/create_purpose - создать цель,\n'
#                          '/update_purpose - обновить цель,\n'
#                          '/clear_purpose - сбросить все старые цели,\n'
#                          '/start_workout - начать тренировку,\n'
#                          '/finish_workout - завершить тренировку,\n'
#                          ''
#                          ''
#                          ''
#                          '/next_workout - ознакомиться с планом на следующую тренировоку,\n'
#                          '/previous_workout - план и факт предыдущей тренировки,\n'
#                          '')