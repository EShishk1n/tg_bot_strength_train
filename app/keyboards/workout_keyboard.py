from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

workout_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Начать тренировку', callback_data='workout_start')],
    [InlineKeyboardButton(text='Информация о тренировках', callback_data='workout_info')],
    [InlineKeyboardButton(text='Рассчитать программу тренировок', callback_data='calculate_workout_program')],
    [InlineKeyboardButton(text='Вернуться в главное меню', callback_data='get_back_to_main_menu')],
])


class WorkoutCallback(CallbackData, prefix='my'):
    workout: str
    exercise_name: str


workout_exercise_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='становая тяга', callback_data=WorkoutCallback(
        workout='workout', exercise_name='становая тяга').pack())],
    [InlineKeyboardButton(text='приседания', callback_data=WorkoutCallback(
        workout='workout', exercise_name='приседания').pack())],
    [InlineKeyboardButton(text='жим лежа', callback_data=WorkoutCallback(
        workout='workout', exercise_name='жим лежа').pack())],
    [InlineKeyboardButton(text='сгибание рук со штангой', callback_data=WorkoutCallback(
        workout='workout', exercise_name='сгибание рук со штангой').pack())],
    [InlineKeyboardButton(text='подтягивания', callback_data=WorkoutCallback(
        workout='workout', exercise_name='подтягивания').pack())],
    [InlineKeyboardButton(text='жим гантелей на наклонной скамье', callback_data=WorkoutCallback(
        workout='workout', exercise_name='жим гантелей в наклоне').pack())],
    [InlineKeyboardButton(text='жим штанги стоя', callback_data=WorkoutCallback(
        workout='workout', exercise_name='жим штанги стоя').pack())],
    [InlineKeyboardButton(text='тяга верхнего блока', callback_data=WorkoutCallback(
        workout='workout', exercise_name='тяга верхнего блока').pack())],
    [InlineKeyboardButton(text='тяга нижнего блока', callback_data=WorkoutCallback(
        workout='workout', exercise_name='тяга нижнего блока').pack())],
    [InlineKeyboardButton(text='Завершить тренировку', callback_data='workout_stop')],
    [InlineKeyboardButton(text='Вернуться в меню "Тренировка"', callback_data='get_back_to_workout_menu')],
])

get_back_to_workout_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вернуться в меню "Тренировка"', callback_data='get_back_to_workout_menu')],
])

delete_previous_workout_program = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Продолжить', callback_data='delete_previous_workout')],
    [InlineKeyboardButton(text='Вернуться в меню "Тренировка"', callback_data='get_back_to_workout_menu')],
])