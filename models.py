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


class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    thread_id = Column(Integer, ForeignKey('thread.id'))
    thread = relationship('Thread', backref='comments')
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship('Comment', backref='comments')
    username = Column(String, nullable=False)
    pwd = Column(String(64), nullable=False)
    content = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.now)
