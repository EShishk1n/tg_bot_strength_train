from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.keyboards.purpose_keyboard import action_with_existing_purpose_keyboard
from app.database.queries import ORMPurpose
from app.handlers.handlers_config import is_right_exercise_format, is_date_format, is_right_purpose_exercise_format
from app.handlers.purpose_handlers.purpose_states import PurposeExercise, DesiredResult, DateReachedAtPlan

from app.keyboards.purpose_keyboard import PurposeCallback, exercise_keyboard

router = Router(name='create_purpose')


# Ловит команду /create_purpose
@router.callback_query(F.data == 'create_purpose')
async def create_purpose(callback: CallbackQuery):
    if await ORMPurpose.is_user_has_purpose(callback.from_user.id):
        current_purpose_data = await ORMPurpose.get_purpose(callback.from_user.id)
        await callback.message.edit_text(
            f'У тебя уже есть цель от {current_purpose_data[0].created_at.date().strftime("%d.%m.%Y")}.\n'
            f'Ты можешь обновить её или удалить.',
            reply_markup=action_with_existing_purpose_keyboard)
    else:
        await ORMPurpose.create_purpose(callback.from_user.id)
        await callback.message.edit_text('Отлично, начало положено!\n'
                                         'Теперь можешь выбрать упражнение и ввести цель',
                                         reply_markup=exercise_keyboard)


# Инициирует запись в цель информации
@router.callback_query(PurposeCallback.filter(F.purpose == 'purpose'))
async def exercise(callback: CallbackQuery, callback_data: PurposeCallback, state: FSMContext):
    await callback.answer('')
    await state.set_state(PurposeExercise.exercise_name)
    exercise_name = callback_data.exercise_name
    await state.update_data(exercise_name=exercise_name)
    await state.set_state(PurposeExercise.exercise_purpose)
    await callback.message.answer(f'Введите цель для упражнения {exercise_name.upper()}\n'
                                  f'Формат записи упражнения - ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ*ЧАСТОТА(раз/неделю)')


# Переключает FSM на exercise_purpose, записывает информацию в БД
@router.message(PurposeExercise.exercise_purpose)
async def exercise_get(message: Message, state: FSMContext):
    if is_right_purpose_exercise_format(message.text):
        await state.update_data(exercise_purpose=message.text)
        tg_id = message.from_user.id
        data = await state.get_data()
        await state.clear()
        await ORMPurpose.save_purpose_exercise(tg_id, data)
        await message.answer(f'Цель для упражнения {data["exercise_name"].upper()} сохранена.\n'
                             f'Выберите следующее упражнение для задания цели из списка',
                             reply_markup=exercise_keyboard)
    else:
        await message.answer('Введите цель по формату ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ*ЧАСТОТА(раз/неделю)')


# Инициирует запись в цель желаемого результата
@router.callback_query(F.data == 'desired_result')
async def desired_result(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(DesiredResult.desired_result)
    await callback.message.answer('Выберите цифру желаемого результата\n'
                                  '1 - похудение с поддержанием физ. формы;\n'
                                  '2 - поддержание физ. формы;\n'
                                  '3 - набор мышечной массы;\n')


# Переключает FSM на desired_result, записывает информацию в БД
@router.message(DesiredResult.desired_result)
async def desired_result_get(message: Message, state: FSMContext):
    if message.text in ('1', '2', '3'):
        await state.update_data(desired_result=message.text)
        user_id = message.from_user.id
        data = await state.get_data()
        await state.clear()
        await ORMPurpose.save_purpose_desired_result(user_id, data)
        await message.answer(f'Желаемый результат {data} сохранен.\n'
                             f'Выберите следующее упражнение для задания цели из списка',
                             reply_markup=exercise_keyboard)
    else:
        await message.answer('Введите желаемый результат с помощью цифр:\n'
                             '1 - похудение с поддержанием физ. формы;\n'
                             '2 - поддержание физ. формы;\n'
                             '3 - набор мышечной массы;\n')


@router.callback_query(F.data == 'date_reached_at_plan')
async def date_reached_at_plan(callback: CallbackQuery, state: FSMContext):
    await callback.answer('')
    await state.set_state(DateReachedAtPlan.date_reached_at_plan)
    await callback.message.answer('Введите планируемую дату достижения цели\n'
                                  'в формате ДД.ММ.ГГГГ')


# Переключает FSM на date_reached_at_plan, записывает информацию в БД
@router.message(DateReachedAtPlan.date_reached_at_plan)
async def date_reached_at_plan_get(message: Message, state: FSMContext):
    if is_date_format(message.text):
        await state.update_data(date_reached_at_plan=message.text)
        user_id = message.from_user.id
        data = await state.get_data()
        await state.clear()
        await ORMPurpose.save_purpose_date_reached_at_plan(user_id, data)
        await message.answer(f'Планируемая дата достижения цели {data["date_reached_at_plan"]} сохранена.\n'
                             f'Выберите следующее упражнение для задания цели из списка',
                             reply_markup=exercise_keyboard)
    else:
        await message.answer('Введите планируемую дату достижения цели\n'
                             'в формате ДД.ММ.ГГГГ')
