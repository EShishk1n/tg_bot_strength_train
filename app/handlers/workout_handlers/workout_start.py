from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from app.handlers.workout_handlers.workout_states import WorkoutExercise
from app.database.queries import ORMWorkout
from app.handlers.handlers_config import is_right_exercise_format

from app.keyboards.workout_keyboard import workout_exercise_keyboard, WorkoutCallback, get_back_to_workout_menu_keyboard

router = Router(name='workout_start')

workout_id = 2


# Ловит команду workout_start
@router.callback_query(F.data == 'workout_start')
async def workout_start(callback: CallbackQuery):
    global workout_id
    workout_id = await ORMWorkout.choose_next_workout()
    purpose_for_current_workout = 'становая столько то, жим столько то ...'
    await callback.message.edit_text(f'Тренировка запущена.\n'
                                     f'Цель на эту тренировку: {purpose_for_current_workout}'
                                     'Выполняй упражнения и записывай результат!\n'
                                     'Для завершения тренировки нажмите соответствующую кнопку',
                                     reply_markup=workout_exercise_keyboard)


# Инициирует запись в тренировку
@router.callback_query(WorkoutCallback.filter(F.workout == 'workout'))
async def workout_exercise(callback: CallbackQuery, callback_data: WorkoutCallback, state: FSMContext):
    await callback.answer('')
    await state.set_state(WorkoutExercise.exercise_name)
    exercise_name = callback_data.exercise_name
    await state.update_data(exercise_name=exercise_name)
    await state.set_state(WorkoutExercise.exercise_workout)
    await callback.message.answer(f'Введите результат выполнения упражнения {exercise_name.upper()}\n'
                                  f'Формат записи упражнения - ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')


# Переключает FSM на exercise_workout, записывает информацию в БД
@router.message(WorkoutExercise.exercise_workout)
async def workout_exercise_get(message: Message, state: FSMContext):
    if is_right_exercise_format(message.text):
        await state.update_data(exercise_workout=message.text)
        data = await state.get_data()
        await state.clear()
        await ORMWorkout.save_workout_exercise(data, workout_id=workout_id)
        await message.answer(f'Результат упражнения {data["exercise_name"].upper()} сохранен.\n'
                             f'Выберите следующее упражнение из списка',
                             reply_markup=workout_exercise_keyboard)
    else:
        await message.answer('Введите цель по формату ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')


@router.callback_query(F.data == 'workout_stop')
async def workout_start(callback: CallbackQuery):
    # await ORMWorkout.workout_stop()
    workout = await ORMWorkout.get_workout(workout_id)
    await callback.message.edit_text(f'Тренировка завершена.\n'
                                     f'Тренировка выполнена на {workout.completion} процентов',
                                     reply_markup=get_back_to_workout_menu_keyboard)
