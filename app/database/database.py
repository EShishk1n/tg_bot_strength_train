from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.database.config import settings

engine = create_async_engine(
    url=settings.database_url_psycopg(),
    # echo=True,
    )

session_factory = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass
