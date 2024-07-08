from aiogram import F, Router
from aiogram.types import CallbackQuery
from aiogram.enums import ParseMode
from tabulate import tabulate

from app.database.models import Workout
from app.database.queries import ORMWorkout
from app.keyboards.workout_keyboard import get_back_to_workout_info_keyboard

router = Router(name='two_workouts_info')


@router.callback_query(F.data.in_(['previous_workout_info', 'next_workout_info']))
async def two_workouts_info(callback: CallbackQuery):
    await callback.answer('')

    if callback.data == 'previous_workout_info':
        # workout_id = await ORMWorkout.choose_next_workout()
        workout_for_presenting_id = 2  # Мокает функцию choose_next_workout()
        message = 'Предыдущая тренировка'
    else:
        # workout_id = await ORMWorkout.choose_next_workout()
        workout_for_presenting_id = 3  # Мокает функцию choose_next_workout()
        message = 'Следующая тренировка'

    workout_for_presenting = await ORMWorkout.get_workout(workout_for_presenting_id)
    data = parse_workout_to_table(w=workout_for_presenting)

    table = tabulate(data, headers="firstrow", tablefmt="grid")

    await callback.message.edit_text(f'{message}\n'
                                     f'<pre>{table}</pre>\n', parse_mode=ParseMode.HTML,
                                     reply_markup=get_back_to_workout_info_keyboard)


def parse_workout_to_table(w: Workout) -> list[list]:
    data = [['Упражнение', 'Цель', 'Факт'],
            ['становая тяга', w.deadlift_plan, w.deadlift_actually],
            ['приседания', w.sqatting_plan, w.sqatting_actually],
            ['жим лежа', w.bench_press_plan, w.bench_press_actually],
            ['сгибание рук со штангой стоя', w.standing_barbell_curl_plan, w.standing_barbell_curl_actually],
            ['подтягивания', w.pull_up_plan, w.pull_up_actually],
            ['жим гантелей на наклонной скамье', w.dumbbell_inclene_bench_press_plan,
             w.dumbbell_inclene_bench_press_actually],
            ['жим стоя', w.military_press_plan, w.military_press_actually],
            ['тяга верхнего блока', w.lat_pull_down_plan, w.lat_pull_down_actually],
            ['тяга нижнего блока', w.seated_row_plan, w.seated_row_actually],
            ]

    return data
