import asyncio
from datetime import datetime
from typing import Tuple, Any

from sqlalchemy import select, text, update

from app.database.database import Base, engine, session_factory
from app.database.models import User, Purpose, Workout


class ORMUser:

    @staticmethod
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def reg_user(user_data):
        async with session_factory() as session:
            user = User(
                tg_id=user_data['tg_id'],
                name=user_data['name'],
                age=int(user_data['age']),
                sex=user_data['sex'],
                weight=float(user_data['weight']),
                height=int(user_data['height']),
                duration_of_const_train=user_data['duration_of_const_train'],
            )
            session.add(user)
            await session.commit()

    @staticmethod
    async def is_user_registered(user_tg_id):
        async with session_factory() as session:
            query = select(User.tg_id).select_from(User)
            result = await session.execute(query)
            if (user_tg_id, ) in result:
                return True
            else:
                return False

    @staticmethod
    async def get_username(user_tg_id: int):
        async with session_factory() as session:
            query = select(User.name).select_from(User).where(User.tg_id == user_tg_id)
            result = await session.execute(query)
            return result.first()[0]

    @staticmethod
    async def update_user(tg_id: int, user_data: dict) -> None:
        async with session_factory() as session:
            query = update(User).where(User.tg_id == tg_id).values(
                age=int(user_data['age']),
                weight=float(user_data['weight']),
                duration_of_const_train=user_data['duration_of_const_train']
            )
            await session.execute(query)
            await session.commit()


class ORMPurpose:

    @staticmethod
    async def is_user_has_purpose(tg_id: int) -> tuple[bool, Any] | bool:
        async with session_factory() as session:
            query = select(Purpose.created_at).where(Purpose.user_id == tg_id)
            result = await session.execute(query)
            purpose = result.first()
            if purpose is not None:
                return True, purpose
            else:
                return False

    @staticmethod
    async def create_purpose(tg_id: int) -> None:
        async with session_factory() as session:
            purpose = Purpose(
                user_id=tg_id
            )
            session.add(purpose)
            await session.commit()

    @staticmethod
    async def save_purpose_exercise(tg_id: int, data: dict) -> None:
        async with session_factory() as session:
            query = select(Purpose).where(Purpose.user_id == tg_id)
            result = await session.execute(query)
            purpose = result.scalars().first()
            exercise_name = data['exercise_name']
            match exercise_name:
                case 'становая тяга':
                    purpose.deadlift = data['exercise_purpose']
                case 'приседания':
                    purpose.sqatting = data['exercise_purpose']
                case 'жим лежа':
                    purpose.bench_press = data['exercise_purpose']
                case 'сгибание рук со штангой':
                    purpose.barbell_curl = data['exercise_purpose']
                case 'подтягивания':
                    purpose.pull_up = data['exercise_purpose']
                case 'жим гантелей в наклоне':
                    purpose.dumbbell_inclene_bench_press = data['exercise_purpose']
                case 'жим штанги стоя':
                    purpose.military_press = data['exercise_purpose']
                case 'тяга верхнего блока':
                    purpose.lat_pull_down = data['exercise_purpose']
                case 'тяга нижнего блока':
                    purpose.seated_row = data['exercise_purpose']
            session.add(purpose)
            await session.commit()


async def main():
    await ORMUser.create_tables()


if __name__ == "__main__":
    asyncio.run(main())
