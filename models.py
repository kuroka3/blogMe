import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Thread(Base):
    __tablename__ = 'thread'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    pwd = Column(String(64), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    like = Column(Integer, nullable=False, default=0)
    unlike = Column(Integer, nullable=False, default=0)
    comments = relationship('Comment', back_populates='thread')


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    thread_id = Column(Integer, ForeignKey('thread.id'), nullable=True)
    thread = relationship('Thread', back_populates='comments')
    comment_id = Column(Integer, ForeignKey('comment.id'), nullable=True)
    comment = relationship('Comment', back_populates='comments', remote_side=[id])
    username = Column(String, nullable=False)
    pwd = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now)
    like = Column(Integer, nullable=False, default=0)
    unlike = Column(Integer, nullable=False, default=0)
    comments = relationship('Comment', back_populates='comment')
