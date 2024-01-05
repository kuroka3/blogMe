from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from models import Thread, Comment


async def get_thread_list(db: AsyncSession):
    thread_list = await db.execute(select(Thread).options(selectinload(Thread.comments).selectinload(Comment.comments))
                                   .order_by(Thread.date.desc()))
    return thread_list.scalars().all()


async def get_thread(db: AsyncSession, __id__: int):
    thread = (await db.execute(select(Thread).options(selectinload(Thread.comments).selectinload(Comment.comments))
                               .where(Thread.id == __id__))).scalar_one_or_none()

    if not thread:
        raise HTTPException(status_code=404)

    thread.view += 1
    await db.commit()
    await db.refresh(thread)

    return thread
