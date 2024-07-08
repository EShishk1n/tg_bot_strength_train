from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

main_keyboard = InlineKeyboardMarkup(inline_keyboard=
                                     [[InlineKeyboardButton(text='Пользователь', callback_data='user')],
                                      [InlineKeyboardButton(text='Цель тренировок', callback_data='purpose')],
                                      [InlineKeyboardButton(text='Тренировка', callback_data='workout')]],
                                     )
