from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from domain.comment import comment_schema, comment_crud
from domain.thread import thread_crud

router = APIRouter(
    prefix="/api/comment",
)


@router.post('/write/thread/{thread_id}')
async def thread_comment_create(thread_id: int, _comment_create: comment_schema.CommentCreate,
                                db: AsyncSession = Depends(get_db)):
    thread = await thread_crud.get_thread(db, thread_id)
    if not thread:
        raise HTTPException(status_code=404, detail=f'Unable to find thread: {thread_id}')

    await comment_crud.create_comment(
        db,
        thread=thread,
        comment_create=_comment_create,
    )


@router.post('/write/comment/{origin_comment_id}')
async def comment_comment_create(origin_comment_id: int, _comment_create: comment_schema.CommentCreate,
                                db: AsyncSession = Depends(get_db)):
    origin_comment = await comment_crud.get_comment(db, origin_comment_id)
    if not origin_comment:
        raise HTTPException(status_code=404, detail=f'Unable to find comment: {origin_comment_id}')

    await comment_crud.create_comment(
        db,
        origin_comment=origin_comment,
        comment_create=_comment_create,
    )
