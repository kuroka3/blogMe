from __future__ import annotations

import datetime

from pydantic import BaseModel, field_validator


class CommentCreate(BaseModel):
    username: str
    pwd: str
    content: str

    @field_validator('content')
    def content_satisfied(cls, v):
        if len(v) < 2:
            raise ValueError('댓글은 2자 이상이어야 합니다.')
        elif len(v) >= 128:
            raise ValueError('댓글은 128자 미만이어야 합니다.')
        else:
            return v

    @field_validator('pwd')
    def pwd_satisfied(cls, v):
        if len(v) < 8 or len(v) >= 32:
            raise ValueError('비밀번호는 8자 이상 32자 미만이어야 합니다.')
        else:
            return v

    @field_validator('username')
    def username_satisfied(cls, v):
        if not v or not v.strip():
            raise ValueError('닉네임은 빌 수 없습니다.')
        else:
            return v


class Comment(BaseModel):
    id: int
    username: str
    content: str
    date: datetime.datetime
    like: int
    unlike: int
    comments: list[Comment] = []
