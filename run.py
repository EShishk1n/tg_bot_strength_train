import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import main_handlers
from app.handlers.purpose_handlers import purpose

from app.handlers.user_handlers import user
from app.handlers.workout_handlers import workout

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(main_handlers.router)
    dp.include_router(user.router)
    dp.include_router(purpose.router)
    dp.include_router(workout.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
