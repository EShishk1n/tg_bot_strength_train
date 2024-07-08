from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.database.queries import ORMPurpose
from app.keyboards.purpose_keyboard import get_back_to_purpose_menu_keyboard, action_with_existing_purpose_keyboard

router = Router(name='current_purpose')


@router.callback_query(F.data == 'current_purpose')
async def current_purpose(callback: CallbackQuery):
    await callback.answer('')
    if await ORMPurpose.is_user_has_purpose(callback.from_user.id):
        current_purpose_query = await ORMPurpose.get_purpose(callback.from_user.id)
        current_purpose_data = current_purpose_query[0]
        current_purpose_exercises = {'становая тяга': current_purpose_data.deadlift,
                                     'приседания': current_purpose_data.sqatting,
                                     'жим лежа': current_purpose_data.bench_press,
                                     'сгибание рук со штангой': current_purpose_data.barbell_curl,
                                     'подтягивания': current_purpose_data.pull_up,
                                     'жим гантелей на наклонной скамье':
                                         current_purpose_data.dumbbell_inclene_bench_press,
                                     'жим штанги стоя': current_purpose_data.military_press,
                                     'тяга верхнего блока': current_purpose_data.lat_pull_down,
                                     'тяга нижнего блока': current_purpose_data.seated_row}
        complition_percentage = 0
        exercises_to_output = ''
        for key, value in current_purpose_exercises.items():
            if value:
                exercises_to_output += f' - {key}: {value}\n'

        await callback.message.edit_text(
            f'Текущая цель от {current_purpose_data.created_at.date().strftime("%d.%m.%Y")}:\n'
            f'{exercises_to_output}'
            f'Цель выполнена на {complition_percentage} процентов',
            reply_markup=action_with_existing_purpose_keyboard)
    else:
        await callback.message.edit_text(f'Цель не задана.\n'
                                         f'Вернитесь в меню "Цель тренировок" и выберите пунки "Задать цель"',
                                         reply_markup=get_back_to_purpose_menu_keyboard)
