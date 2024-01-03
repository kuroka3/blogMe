from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

import hash
from domain.comment.comment_schema import CommentCreate
from models import Thread, Comment


async def create_comment(db: AsyncSession, comment_create: CommentCreate,
                         thread: Thread = None, origin_comment: Comment = None):
    db_comment = Comment(
        thread=thread,
        comment=origin_comment,
        username=comment_create.username,
        pwd=await hash.hash_sha256(comment_create.pwd),
        content=comment_create.content
    )
    db.add(db_comment)
    await db.commit()


async def get_comment(db: AsyncSession, __id__: int):
    comment = await db.execute(select(Comment).options(selectinload(Comment.comments)).where(Comment.id == __id__))
    return comment.scalar()
