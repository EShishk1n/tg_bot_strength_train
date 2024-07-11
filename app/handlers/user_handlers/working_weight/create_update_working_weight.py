from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from app.database.queries import ORMWorkingWeight

from app.keyboards.user_keyboard import get_back_to_user_menu_keyboard

router = Router(name='create_update_working_weight')


# Ловит команду /create_update_working_weight
@router.callback_query(F.data == 'create_update_working_weight')
async def create_update_working_weight(callback: CallbackQuery):
    await callback.answer('')
    if await ORMWorkingWeight.get_working_weight(callback.from_user.id):
        await ORMWorkingWeight.delete_working_weight(callback.from_user.id)
    await ORMWorkingWeight.create_working_weight(callback.from_user.id)
    await callback.message.edit_text('Скопируй текст ниже и добавь туда свои рабочие веса:\n'
                                     'становая тяга:\n'
                                     'приседания:\n'
                                     'жим лежа:\n'
                                     'сгибание рук со штангой:\n'
                                     'подтягивания:\n'
                                     'жим гантелей в наклоне:\n'
                                     'жим штанги стоя:\n'
                                     'тяга верхнего блока:\n'
                                     'тяга нижнего блока:\n')


# Принимает список упражнений с рабочими весами и записывает информацию в БД
@router.message(F.text.startswith('становая тяга:'))
async def working_weight_get(message: Message):
    data = {}
    for str_ in message.text.split('\n'):
        exercise_name = str_.split(':')[0]
        if str_.split(':')[1]:
            working_weight = int(str_.split(':')[1])
        else:
            working_weight = 0
        data[exercise_name] = working_weight
    await ORMWorkingWeight.save_working_weight(message.from_user.id, data)
    await message.answer(f'Информация о рабочем весе сохранена', reply_markup=get_back_to_user_menu_keyboard)
