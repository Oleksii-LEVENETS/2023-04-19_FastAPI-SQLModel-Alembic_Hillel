import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from sqlmodel import SQLModel


DATABASE_URL = os.environ.get("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, echo=True, future=True)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session


##########
# import os
#
# from sqlmodel import create_engine, SQLModel, Session
#
#
# DATABASE_URL = os.environ.get("DATABASE_URL")
#
# engine = create_engine(DATABASE_URL, echo=True)
#
#
# def init_db():
#     SQLModel.metadata.create_all(engine)
#
#
# def get_session():
#     with Session(engine) as session:
#         yield session
