from aiogram import Router, F
from aiogram.types import CallbackQuery, FSInputFile

from app.database.queries import ORMPurpose, ORMWorkout, ORMWorkingWeight
from app.keyboards.workout_keyboard import workout_keyboard, delete_previous_workout_program
from app.services.calculate_workout_program.calculate_workout_program import pick_data_for_calculation_workout_program
from app.services.calculate_workout_program.class_for_calculation_workout_program import WorkoutProgramCalculation
from app.services.calculate_workout_program.get_exercises_without_purpose import get_exercises_with_purpose
from app.services.make_xlsx_file.make_xlsx_file import create_file_with_all_workouts_info

router = Router(name='calculate_workout_program')


@router.callback_query(F.data == 'calculate_workout_program')
async def calculate_workout_program(callback: CallbackQuery):
    await callback.answer('')
    if await ORMWorkout.has_unfinished_workout(callback.from_user.id):
        await callback.message.edit_text('У вас остались незавершенные тренировки.\n'
                                         'При расчете новой программы все они будут удалены. Продолжить?',
                                         reply_markup=delete_previous_workout_program)
    else:
        user_id = callback.from_user.id
        purpose = await ORMPurpose.get_purpose(user_id)
        working_weight = await ORMWorkingWeight.get_working_weight(user_id)
        exercises_with_purpose = get_exercises_with_purpose(purpose[0])
        for exercise in exercises_with_purpose:
            data = await pick_data_for_calculation_workout_program(purpose[0], working_weight[0], exercise)
            workout_program = WorkoutProgramCalculation(current_exercise=data['current_exercise'],
                                                        purpose_exercise=data['purpose_exercise'],
                                                        date_reached_at_plan=data['date_reached_at_plan'],
                                                        desired_result=data['desired_result']).calculate_workout_program()
            await ORMWorkout.insert_workout_program(user_id, exercise, workout_program)
        filename = await create_file_with_all_workouts_info(callback.from_user.id)
        input_file = FSInputFile(filename)
        await callback.message.edit_text('Программа тренировок рассчитана.',
                                         reply_markup=workout_keyboard)
        await callback.message.reply_document(document=input_file)


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
