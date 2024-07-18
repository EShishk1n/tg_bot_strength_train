from datetime import datetime

from sqlalchemy import BigInteger, String, Integer, Float, text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class User(Base):
    __tablename__ = 'users'

    tg_id = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(25))
    age: Mapped[int] = mapped_column(Integer)
    sex: Mapped[str]
    weight: Mapped[float] = mapped_column(Float)
    height: Mapped[int] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    def __repr__(self) -> str:
        return f'User(name={self.name}, age={self.age}'


class WorkingWeight(Base):
    __tablename__ = 'weights'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id', ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    deadlift: Mapped[int] = mapped_column(nullable=True)
    squatting: Mapped[int] = mapped_column(nullable=True)
    bench_press: Mapped[int] = mapped_column(nullable=True)
    barbell_curl: Mapped[int] = mapped_column(nullable=True)
    pull_up: Mapped[int] = mapped_column(nullable=True)
    dumbbell_inclene_bench_press: Mapped[int] = mapped_column(nullable=True)
    military_press: Mapped[int] = mapped_column(nullable=True)
    lat_pull_down: Mapped[int] = mapped_column(nullable=True)
    seated_row: Mapped[int] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (f'становая тяга:{self.deadlift}\nприседания: {self.squatting}\nжим лежа: {self.bench_press}\n'
                f'сгибание рук со штангой: {self.barbell_curl}\nподтягивания: {self.pull_up}\n'
                f'жим гантелей в наклоне: {self.dumbbell_inclene_bench_press}\nжим штанги стоя: {self.military_press}\n'
                f'тяга верхнего блока: {self.seated_row}\nтяга нижнего блока: {self.lat_pull_down}\n')


class Purpose(Base):
    __tablename__ = 'purposes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id', ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    deadlift: Mapped[str] = mapped_column(nullable=True)
    squatting: Mapped[str] = mapped_column(nullable=True)
    bench_press: Mapped[str] = mapped_column(nullable=True)
    standing_barbell_curl: Mapped[str] = mapped_column(nullable=True)
    pull_up: Mapped[str] = mapped_column(nullable=True)
    dumbbell_incline_bench_press: Mapped[str] = mapped_column(nullable=True)
    military_press: Mapped[str] = mapped_column(nullable=True)
    lat_pull_down: Mapped[str] = mapped_column(nullable=True)
    seated_row: Mapped[str] = mapped_column(nullable=True)
    date_reached_at_plan: Mapped[datetime] = mapped_column(nullable=True)
    desired_result: Mapped[str] = mapped_column(nullable=True)
    date_reached_at_actually: Mapped[datetime] = mapped_column(nullable=True)

    def __repr__(self):
        return f'цель поставлена {self.created_at} для {self.user_id}'


class WorkoutBase:
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id', ondelete="CASCADE"))
    plan: Mapped[str] = mapped_column(nullable=True)
    fact: Mapped[str] = mapped_column(nullable=True, default='')

    def __repr__(self) -> str:
        return f'plan={self.plan}, fact={self.fact}'


class Deadlift(Base, WorkoutBase):
    __tablename__ = 'deadlift'


class Squatting(Base, WorkoutBase):
    __tablename__ = 'squatting'


class BenchPress(Base, WorkoutBase):
    __tablename__ = 'bench_press'


class StandingBarbellCurl(Base, WorkoutBase):
    __tablename__ = 'standing_barbell_curl'


class PullUp(Base, WorkoutBase):
    __tablename__ = 'pull_up'


class DumbbellInclineBenchPress(Base, WorkoutBase):
    __tablename__ = 'dumbbell_incline_bench_press'


class MilitaryPress(Base, WorkoutBase):
    __tablename__ = 'military_press'


class LatPullDown(Base, WorkoutBase):
    __tablename__ = 'lat_pull_down'


class SeatedRow(Base, WorkoutBase):
    __tablename__ = 'seated_row'

# class Workout(Base):
#     __tablename__ = 'workouts'
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     number: Mapped[int]
#     user_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id', ondelete="CASCADE"))
#     purpose: Mapped[int] = mapped_column(ForeignKey('purposes.id', ondelete="CASCADE"))
#     created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
#     deadlift_plan: Mapped[str] = mapped_column(nullable=True)
#     deadlift_actually: Mapped[str] = mapped_column(nullable=True)
#     sqatting_plan: Mapped[str] = mapped_column(nullable=True)
#     sqatting_actually: Mapped[str] = mapped_column(nullable=True)
#     bench_press_plan: Mapped[str] = mapped_column(nullable=True)
#     bench_press_actually: Mapped[str] = mapped_column(nullable=True)
#     standing_barbell_curl_plan: Mapped[str] = mapped_column(nullable=True)
#     standing_barbell_curl_actually: Mapped[str] = mapped_column(nullable=True)
#     pull_up_plan: Mapped[str] = mapped_column(nullable=True)
#     pull_up_actually: Mapped[str] = mapped_column(nullable=True)
#     dumbbell_inclene_bench_press_plan: Mapped[str] = mapped_column(nullable=True)
#     dumbbell_inclene_bench_press_actually: Mapped[str] = mapped_column(nullable=True)
#     military_press_plan: Mapped[str] = mapped_column(nullable=True)
#     military_press_actually: Mapped[str] = mapped_column(nullable=True)
#     lat_pull_down_plan: Mapped[str] = mapped_column(nullable=True)
#     lat_pull_down_actually: Mapped[str] = mapped_column(nullable=True)
#     seated_row_plan: Mapped[str] = mapped_column(nullable=True)
#     seated_row_actually: Mapped[str] = mapped_column(nullable=True)
#     reached_at_plan: Mapped[datetime] = mapped_column(nullable=True)
#     reached_at_actually: Mapped[datetime] = mapped_column(nullable=True)
#     completion: Mapped[int] = mapped_column(nullable=True)
#     status: Mapped[str] = mapped_column(nullable=False, default='waiting')
#     comment: Mapped[str] = mapped_column(nullable=True)
#
#     def __repr__(self):
#         return f'тренировка от {self.created_at} выполнена на {self.completion} процентов'
