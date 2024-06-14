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
    duration_of_const_train: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))

    def __repr__(self) -> str:
        return f'User(name={self.name}, age={self.age}, strength_level={self.duration_of_const_train}'


# print(User.__table__)


class Purpose(Base):
    __tablename__ = 'purposes'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id', ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    deadlift: Mapped[str] = mapped_column(nullable=True)
    sqatting: Mapped[str] = mapped_column(nullable=True)
    bench_press: Mapped[str] = mapped_column(nullable=True)
    barbell_curl: Mapped[str] = mapped_column(nullable=True)
    pull_up: Mapped[str] = mapped_column(nullable=True)
    dumbbell_inclene_bench_press: Mapped[str] = mapped_column(nullable=True)
    military_press: Mapped[str] = mapped_column(nullable=True)
    lat_pull_down: Mapped[str] = mapped_column(nullable=True)
    seated_row: Mapped[str] = mapped_column(nullable=True)
    reached_at: Mapped[datetime] = mapped_column(nullable=True)

    def __repr__(self):
        return f'цель поставлена {self.created_at} для {self.user_id}'


class Workout(Base):
    __tablename__ = 'workouts'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.tg_id', ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    deadlift_plan: Mapped[str] = mapped_column(nullable=True)
    deadlift_actually: Mapped[str] = mapped_column(nullable=True)
    sqatting_plan: Mapped[str] = mapped_column(nullable=True)
    sqatting_actually: Mapped[str] = mapped_column(nullable=True)
    bench_press_plan: Mapped[str] = mapped_column(nullable=True)
    bench_press_actually: Mapped[str] = mapped_column(nullable=True)
    standing_barbell_curl_plan: Mapped[str] = mapped_column(nullable=True)
    standing_barbell_curl_actually: Mapped[str] = mapped_column(nullable=True)
    pull_up_plan: Mapped[str] = mapped_column(nullable=True)
    pull_up_actually: Mapped[str] = mapped_column(nullable=True)
    dumbbell_inclene_bench_press_plan: Mapped[str] = mapped_column(nullable=True)
    dumbbell_inclene_bench_press_actually: Mapped[str] = mapped_column(nullable=True)
    military_press_plan: Mapped[str] = mapped_column(nullable=True)
    military_press_actually: Mapped[str] = mapped_column(nullable=True)
    lat_pull_down_plan: Mapped[str] = mapped_column(nullable=True)
    lat_pull_down_actually: Mapped[str] = mapped_column(nullable=True)
    seated_row_plan: Mapped[str] = mapped_column(nullable=True)
    seated_row_actually: Mapped[str] = mapped_column(nullable=True)
    reached_at_plan: Mapped[datetime] = mapped_column(nullable=True)
    reached_at_actually: Mapped[datetime] = mapped_column(nullable=True)
    completion: Mapped[int] = mapped_column(nullable=True)
    comment: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self):
        return f'тренировка от {self.created_at} выполнена на {self.completion} процентов'
