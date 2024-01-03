from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Thread, Comment


async def get_thread_list(db: AsyncSession):
    thread_list = await db.execute(select(Thread).options(selectinload(Thread.comments).selectinload(Comment.comments))
                                   .order_by(Thread.date.desc()))
    return thread_list.scalars().all()


async def get_thread(db: AsyncSession, __id__: int):
    thread = await db.execute(select(Thread).options(selectinload(Thread.comments).selectinload(Comment.comments))
                              .where(Thread.id == __id__))
    return thread.scalar_one()
