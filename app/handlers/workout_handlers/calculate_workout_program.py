from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.database.queries import ORMPurpose, ORMWorkout
from app.keyboards.workout_keyboard import workout_keyboard, delete_previous_workout_program

router = Router(name='calculate_workout_program')


@router.callback_query(F.data == 'calculate_workout_program')
async def calculate_workout_program(callback: CallbackQuery):
    if await ORMWorkout.is_user_has_unfinished_workout(callback.from_user.id):
        await callback.message.edit_text('У вас остались незавершенные тренировки. '
                                         'При расчете новой программы все они будут удалены. Продолжить?',
                                         reply_markup=delete_previous_workout_program)
    else:


        await callback.message.edit_text('Вы перешли в блок "Тренировка"\n'
                                         f'Вернитесь в основное меню, выберите пункт "Цель тренировок", "Задать цель"',
                                         reply_markup=workout_keyboard)


@router.callback_query(F.data == 'delete_previous_workout')
async def delete_previous_workout(callback: CallbackQuery):
    await ORMWorkout.delete_unfinished_workout(callback.from_user.id)
    await callback.message.edit_text('Незавершенные тренировки удалены.\n'
                                     'Вы перешли в блок "Тренировка"\n'
                                     'Выберите пункт:', reply_markup=workout_keyboard)


@router.callback_query(F.data == 'get_back_to_workout_menu')
async def get_back_to_workout_menu(callback: CallbackQuery):
    await callback.message.edit_text('Вы перешли в блок "Тренировка"\n'
                                     'Выберите пункт:', reply_markup=workout_keyboard)
