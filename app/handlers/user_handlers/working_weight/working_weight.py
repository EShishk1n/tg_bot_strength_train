from aiogram import Router, F
from aiogram.types import CallbackQuery

from app.database.queries import ORMWorkingWeight, ORMUser
from app.keyboards.user_keyboard import actions_with_working_weight

router = Router(name='working_weight')


@router.callback_query(F.data == 'working_weight')
async def working_weight(callback: CallbackQuery):
    await callback.answer('')
    working_weight_info = await ORMWorkingWeight.get_working_weight(callback.from_user.id)
    username = await ORMUser.get_user_info(callback.from_user.id)
    if working_weight_info:
        await callback.message.edit_text(f'Рабочие веса для пользователя {username[0].name}:\n'
                                         f'{working_weight_info[0]}', reply_markup=actions_with_working_weight)
    else:
        await callback.message.edit_text(f'Рабочие веса для пользователя {callback.from_user.username} не заданы.\n'
                                         'Для возможности расчета программы тренировок добавьте информацию о рабочих '
                                         'весах:', reply_markup=actions_with_working_weight)
