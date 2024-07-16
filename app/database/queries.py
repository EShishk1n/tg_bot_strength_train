import asyncio
from datetime import datetime

from sqlalchemy import select, text, update, delete

from app.database.database import Base, engine, session_factory
from app.database.models import User, Purpose, Workout, WorkingWeight


class ORMUser:

    @staticmethod
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            # await conn.run_sync(Base.metadata.create_all)

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
            )
            session.add(user)
            await session.commit()

    @staticmethod
    async def is_user_registered(user_tg_id):
        async with session_factory() as session:
            query = select(User.tg_id).select_from(User)
            result = await session.execute(query)
            if (user_tg_id,) in result:
                return True
            else:
                return False

    @staticmethod
    async def get_user_info(user_tg_id: int) -> User:
        async with session_factory() as session:
            query = select(User).where(User.tg_id == user_tg_id)
            result = await session.execute(query)
            return result.first()

    @staticmethod
    async def update_user(tg_id: int, user_data: dict) -> None:
        async with session_factory() as session:
            query = select(User).where(User.tg_id == tg_id)
            result = await session.execute(query)
            user = result.scalars().first()
            param_for_updating = list(user_data.keys())
            match param_for_updating[0]:
                case 'age':
                    user.age = list(user_data.values())[0]
                case 'weight':
                    user.weight = list(user_data.values())[0]
            session.add(user)
            await session.commit()


class ORMPurpose:

    @staticmethod
    async def is_user_has_purpose(tg_id: int) -> bool:
        async with session_factory() as session:
            query = select(Purpose).where(Purpose.user_id == tg_id)
            result = await session.execute(query)
            if result.first() is not None:
                return True
            else:
                return False

    @staticmethod
    async def get_purpose(user_id: int) -> Purpose:
        async with session_factory() as session:
            query = select(Purpose).where(Purpose.user_id == user_id)
            result = await session.execute(query)
            purpose = result.first()
            return purpose

    @staticmethod
    async def delete_purpose(tg_id: int) -> None:
        async with engine.begin() as conn:
            query = delete(Purpose).where(Purpose.user_id == tg_id)
            await conn.execute(query)

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

    @staticmethod
    async def save_purpose_desired_result(user_id: int, data: dict) -> None:
        async with session_factory() as session:
            query = select(Purpose).where(Purpose.user_id == user_id)
            result = await session.execute(query)
            purpose = result.scalars().first()
            desired_result = data['desired_result']
            match desired_result:
                case '1':
                    purpose.desired_result = 'похудение с поддержанием физ. формы'
                case '2':
                    purpose.desired_result = 'поддержание физ. формы'
                case '3':
                    purpose.desired_result = 'набор мышечной массы'
            session.add(purpose)
            await session.commit()

    @staticmethod
    async def save_purpose_date_reached_at_plan(user_id: int, data: dict) -> None:
        async with session_factory() as session:
            query = select(Purpose).where(Purpose.user_id == user_id)
            result = await session.execute(query)
            purpose = result.scalars().first()
            purpose.date_reached_at_plan = datetime.strptime(data['date_reached_at_plan'], '%d.%m.%Y')
            session.add(purpose)
            await session.commit()


class ORMWorkout:
    @staticmethod
    async def get_workout(workout_id: int) -> Workout:
        async with session_factory() as session:
            query = select(Workout).where(Workout.id == workout_id)
            result = await session.execute(query)
            workout = result.first()[0]
            return workout

    @staticmethod
    async def get_all_workouts():
        async with session_factory() as session:
            query = select(Workout)
            result = await session.execute(query)
            workouts = result.all()
            return workouts

    @staticmethod
    async def choose_next_workout() -> Workout.id:
        async with session_factory() as session:
            query = select(Workout.id).where(Workout.status == 'waiting')
            result = await session.execute(query)
            return result.scalars().first()

    @staticmethod
    async def save_workout_exercise(data: dict, workout_id: Workout.id) -> None:
        async with session_factory() as session:
            query = select(Workout).where(Workout.id == workout_id)
            result = await session.execute(query)
            workout = result.scalars().first()
            exercise_name = data['exercise_name']
            match exercise_name:
                case 'становая тяга':
                    workout.deadlift_actually = data['exercise_workout']
                case 'приседания':
                    workout.sqatting_actually = data['exercise_workout']
                case 'жим лежа':
                    workout.bench_press_actually = data['exercise_workout']
                case 'сгибание рук со штангой':
                    workout.barbell_curl_actually = data['exercise_workout']
                case 'подтягивания':
                    workout.pull_up_actually = data['exercise_workout']
                case 'жим гантелей в наклоне':
                    workout.dumbbell_inclene_bench_press_actually = data['exercise_workout']
                case 'жим штанги стоя':
                    workout.military_press_actually = data['exercise_workout']
                case 'тяга верхнего блока':
                    workout.lat_pull_down_actually = data['exercise_workout']
                case 'тяга нижнего блока':
                    workout.seated_row_actually = data['exercise_workout']
            session.add(workout)
            await session.commit()

    @staticmethod
    async def is_user_has_unfinished_workout(user_id) -> bool:
        async with session_factory() as session:
            query = select(Workout).where(Workout.user_id == user_id, Workout.status == 'waiting')
            result = await session.execute(query)
            if result.first() is not None:
                return True
            else:
                return False

    @staticmethod
    async def delete_unfinished_workout(user_id) -> None:
        async with engine.begin() as conn:
            query = delete(Workout).where(Workout.user_id == user_id, Workout.status == 'waiting')
            await conn.execute(query)


class ORMWorkingWeight:
    @staticmethod
    async def get_working_weight(user_id: int) -> WorkingWeight:
        async with session_factory() as session:
            query = select(WorkingWeight).where(WorkingWeight.user_id == user_id)
            result = await session.execute(query)
            working_weight = result.first()
            return working_weight

    @staticmethod
    async def delete_working_weight(user_id: int) -> None:
        async with engine.begin() as conn:
            query = delete(WorkingWeight).where(WorkingWeight.user_id == user_id)
            await conn.execute(query)

    @staticmethod
    async def create_working_weight(user_id: int) -> None:
        async with session_factory() as session:
            working_weight = WorkingWeight(
                user_id=user_id
            )
            session.add(working_weight)
            await session.commit()

    @staticmethod
    async def save_working_weight(user_id: int, data: dict) -> None:
        async with session_factory() as session:
            query = select(WorkingWeight).where(WorkingWeight.user_id == user_id)
            result = await session.execute(query)
            working_weight = result.scalars().first()
            for exercise in data.items():
                match exercise[0]:
                    case 'становая тяга':
                        working_weight.deadlift = exercise[1]
                    case 'приседания':
                        working_weight.sqatting = exercise[1]
                    case 'жим лежа':
                        working_weight.bench_press = exercise[1]
                    case 'сгибание рук со штангой':
                        working_weight.barbell_curl = exercise[1]
                    case 'подтягивания':
                        working_weight.pull_up = exercise[1]
                    case 'жим гантелей в наклоне':
                        working_weight.dumbbell_inclene_bench_press = exercise[1]
                    case 'жим штанги стоя':
                        working_weight.military_press = exercise[1]
                    case 'тяга верхнего блока':
                        working_weight.lat_pull_down = exercise[1]
                    case 'тяга нижнего блока':
                        working_weight.seated_row = exercise[1]
            session.add(working_weight)
            await session.commit()


async def main():
    await ORMUser.create_tables()


if __name__ == "__main__":
    asyncio.run(main())
