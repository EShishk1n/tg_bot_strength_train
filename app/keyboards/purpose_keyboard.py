from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class PurposeCallback(CallbackData, prefix='my'):
    purpose: str
    exercise_name: str


exercise_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='становая тяга', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='становая тяга').pack())],
    [InlineKeyboardButton(text='приседания', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='приседания').pack())],
    [InlineKeyboardButton(text='жим лежа', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='жим лежа').pack())],
    [InlineKeyboardButton(text='сгибание рук со штангой', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='сгибание рук со штангой').pack())],
    [InlineKeyboardButton(text='подтягивания', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='подтягивания').pack())],
    [InlineKeyboardButton(text='жим гантелей на наклонной скамье', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='жим гантелей в наклоне').pack())],
    [InlineKeyboardButton(text='жим штанги стоя', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='жим штанги стоя').pack())],
    [InlineKeyboardButton(text='тяга верхнего блока', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='тяга верхнего блока').pack())],
    [InlineKeyboardButton(text='тяга нижнего блока', callback_data=PurposeCallback(
        purpose='purpose', exercise_name='тяга нижнего блока').pack())],
])



action_with_existing_purpose_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='обновить цель', callback_data='update_purpose')],
    [InlineKeyboardButton(text='удалить цель', callback_data='clear_purpose')],
])

