# from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./blogme.db'
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
Base = declarative_base()
#
#
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


ASYNC_SQLALCHEMY_DATABASE_URL = 'sqlite+aiosqlite:///./blogme.db'

async_engine = create_async_engine(ASYNC_SQLALCHEMY_DATABASE_URL)


async def get_db():
    db = AsyncSession(bind=async_engine)
    try:
        yield db
    finally:
        await db.close()
