from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from tabulate import tabulate

from app.handlers.workout_handlers.workout_states import WorkoutExercise
from app.database.queries import ORMWorkout
from app.handlers.handlers_config import is_right_exercise_format, exercise_dict

from app.keyboards.workout_keyboard import workout_exercise_keyboard, WorkoutCallback, get_back_to_workout_menu_keyboard

router = Router(name='workout_start')


# Ловит команду workout_start
@router.callback_query(F.data == 'workout_start')
async def workout_start(callback: CallbackQuery):
    purpose_for_current_workout = await ORMWorkout.make_workout(callback.from_user.id)
    data = parse_workout_to_table(w=purpose_for_current_workout)
    table = tabulate(data, headers="firstrow", tablefmt="grid")
    message = 'Тренировка запущена. Цель на эту тренировку:\n'
    message1 = 'Выполняй упражнения и записывай результат!\nДля завершения тренировки нажмите соответствующую кнопку'
    await callback.message.edit_text(f'{message}\n'
                                     f'<pre>{table}</pre>\n'
                                     f'{message1}', parse_mode=ParseMode.HTML,
                                     reply_markup=workout_exercise_keyboard)


def parse_workout_to_table(w: dict) -> list[list]:

    data = [['Упражнение', 'Цель', 'Факт'],]
    for exercise in list(w.items()):
        if exercise[1] is not None:
            data.append([exercise_dict[exercise[0]], exercise[1].plan, exercise[1].fact])

    return data


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
        await ORMWorkout.save_workout_exercise(data, user_id=message.from_user.id)
        await message.answer(f'Результат упражнения {data["exercise_name"].upper()} сохранен.\n'
                             f'Выберите следующее упражнение из списка',
                             reply_markup=workout_exercise_keyboard)
    else:
        await message.answer('Введите цель по формату ВЕС*ПОВТОРЕНИЯ*ПОДХОДЫ')


@router.callback_query(F.data == 'workout_stop')
async def workout_stop(callback: CallbackQuery):
    await callback.answer('')
    workout = await ORMWorkout.get_last_workout(callback.from_user.id)
    data = parse_workout_to_table(w=workout)
    table = tabulate(data, headers="firstrow", tablefmt="grid")
    message = 'Тренировка завершена.\n'
    await callback.message.edit_text(f'{message}\n'
                                     f'<pre>{table}</pre>\n',
                                     parse_mode=ParseMode.HTML,
                                     reply_markup=get_back_to_workout_menu_keyboard)
