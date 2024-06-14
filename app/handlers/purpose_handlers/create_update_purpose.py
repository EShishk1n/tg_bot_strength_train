from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.handlers.purpose_handlers.purpose import router
from app.keyboards.purpose_keyboard import action_with_existing_purpose_keyboard
from app.database.queries import ORMPurpose
from app.handlers.handlers_config import is_right_exercise_format
from app.handlers.purpose_handlers.purpose_states import PurposeExercise

from app.keyboards.purpose_keyboard import PurposeCallback, exercise_keyboard


# Ловит команду /create_purpose
@router.message(Command('create_purpose'))
async def cmd_start(message: Message):
    if await ORMPurpose.is_user_has_purpose(message.from_user.id):
        purpose_created_at = await ORMPurpose.is_user_has_purpose(message.from_user.id)
        await message.answer(f'У тебя уже есть цель от {purpose_created_at[1][0].date().strftime("%d.%m.%Y")}.\n'
                             f'Ты можешь обновить её или удалить.',
                             reply_markup=action_with_existing_purpose_keyboard)
    else:
        await ORMPurpose.create_purpose(message.from_user.id)
        await message.answer('Отлично, начало положено!\n'
                             'Теперь можешь выбрать упражнение и ввести цель',
                             reply_markup=exercise_keyboard)


# Инициирует запись в цель информации
@router.callback_query(PurposeCallback.filter(F.purpose == 'purpose'))
async def deadlift(callback: CallbackQuery, callback_data: PurposeCallback, state: FSMContext):
    await callback.answer('')
    await state.set_state(PurposeExercise.exercise_name)
    exercise_name = callback_data.exercise_name
    await state.update_data(exercise_name=exercise_name)
    await state.set_state(PurposeExercise.exercise_purpose)
    await callback.message.answer(f'Введите цель для упражнения {exercise_name.upper()}\n'
                                  f'Формат записи упражнения - ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')


# Переключает FSM на exercise_purpose, записывает информацию в БД
@router.message(PurposeExercise.exercise_purpose)
async def deadlift_get(message: Message, state: FSMContext):
    if is_right_exercise_format(message.text):
        await state.update_data(exercise_purpose=message.text)
        tg_id = message.from_user.id
        data = await state.get_data()
        await ORMPurpose.save_purpose_exercise(tg_id, data)
        await message.answer(f'Цель для упражнения {data["exercise_name"].upper()} сохранена.\n'
                             f'Выберите следующее упражнение для задания цели из списка',
                             reply_markup=exercise_keyboard)
    else:
        await message.answer('Введите цель по формату ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')
