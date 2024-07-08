import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import main_handlers
from app.handlers.purpose_handlers import purpose, current_purpose, create_purpose, delete_purpose, update_purpose

from app.handlers.user_handlers import user, user_info, user_registration, user_updation
from app.handlers.workout_handlers import workout
from app.handlers.workout_handlers import workout_start
from app.handlers.workout_handlers.workout_info import workout_info, two_workouts_info
from app.handlers.workout_handlers.workout_info import all_workouts_info

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(main_handlers.router)
    dp.include_routers(user.router, user_info.router, user_registration.router, user_updation.router)
    dp.include_routers(purpose.router, current_purpose.router, create_purpose.router, delete_purpose.router,
                       update_purpose.router)
    dp.include_routers(workout.router, workout_start.router, workout_info.router, two_workouts_info.router,
                       all_workouts_info.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
