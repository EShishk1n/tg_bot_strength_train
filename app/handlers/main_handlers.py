from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from app.database.queries import ORMUser
from app.keyboards.main_keyboard import main_keyboard

router = Router(name='main_handlers')


# Ловит команду /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    if await ORMUser.is_user_registered(message.from_user.id):
        user_info = await ORMUser.get_user_info(message.from_user.id)
        await message.answer(f'С возвращением, {user_info[0].name}!\n'
                             f'Для продолжения тренировок предлагаю проверить актуальность информации в блоке'
                             f'"Пользователь" и "Цель тренировок"',
                             reply_markup=main_keyboard)
    else:
        await message.answer(
            f'Привет!\nЭто бот для контроля силовых тренировок.\n'
            f'Для начала тренировок зарегистрируйся в блоке "Пользователь"',
            reply_markup=main_keyboard)


# ловит команду возвращения в основное меню
@router.callback_query(F.data == 'get_back_to_main_menu')
async def user(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Вы перешли в Основное меню',
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
