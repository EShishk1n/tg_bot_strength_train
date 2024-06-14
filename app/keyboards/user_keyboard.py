from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder



# Reply keyboard
start_keyboard = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text='Начать регистрацию')]],
    resize_keyboard=True)

update_user_data_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Обновить данные')]],
    resize_keyboard=True,
    one_time_keyboard=True)


sex_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str('Мужской'))],
    [KeyboardButton(text=str('Женский'))]
],
    resize_keyboard=True,
    one_time_keyboard=True,)


duration_of_const_train_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='только начинаю')],
    [KeyboardButton(text='более 3 месяцев')],
    [KeyboardButton(text='более года')],
    [KeyboardButton(text='более 3 лет')],],
    resize_keyboard=True,
    one_time_keyboard=True)