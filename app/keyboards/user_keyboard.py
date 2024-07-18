from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

user_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Информация о пользователе', callback_data='user_info')],
    [InlineKeyboardButton(text='Начать регистрацию', callback_data='user_registration')],
    [InlineKeyboardButton(text='Обновить информацию', callback_data='user_updation')],
    [InlineKeyboardButton(text='Рабочие веса', callback_data='working_weight')],
    [InlineKeyboardButton(text='Вернуться в главное меню', callback_data='get_back_to_main_menu')],
])


get_back_to_user_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться в меню пользователя', callback_data='get_back_to_user_menu')],
])


sex_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=str('Мужской'))],
    [KeyboardButton(text=str('Женский'))]
],
    resize_keyboard=True,
    one_time_keyboard=True)

duration_of_const_train_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='только начинаю')],
    [KeyboardButton(text='более 3 месяцев')],
    [KeyboardButton(text='более года')],
    [KeyboardButton(text='более 3 лет')], ],
    resize_keyboard=True,
    one_time_keyboard=True)

params_for_updating_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Возраст', callback_data='update_age')],
    [InlineKeyboardButton(text='Вес', callback_data='update_weight')],
    [InlineKeyboardButton(text='Вернуться в меню пользователя', callback_data='get_back_to_user_menu')],
])

actions_with_working_weight = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Добавить/обновить информацию', callback_data='create_update_working_weight')],
    [InlineKeyboardButton(text='Вернуться в меню пользователя', callback_data='get_back_to_user_menu')],
])
