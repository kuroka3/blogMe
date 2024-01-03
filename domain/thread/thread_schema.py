import datetime

from pydantic import BaseModel

from domain.comment.comment_schema import Comment


class Thread(BaseModel):
    id: int
    username: str
    title: str
    content: str
    date: datetime.datetime
    like: int
    unlike: int
    comments: list[Comment] = []
