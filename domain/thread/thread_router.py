from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from domain.thread import thread_schema, thread_crud

router = APIRouter(
    prefix="/api/thread",
)


@router.get('/list', response_model=list[thread_schema.Thread])
async def thread_list(db: AsyncSession = Depends(get_db)):
    _thread_list = await thread_crud.get_thread_list(db)
    return _thread_list


@router.get('/{__id__}', response_model=thread_schema.Thread)
async def thread(__id__: int, db: AsyncSession = Depends(get_db)):
    _thread = await thread_crud.get_thread(db, __id__)
    return _thread
