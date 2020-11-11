from sqlalchemy import Table, Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime
from pytz import timezone

from .base import Base


class Answers(Base):
    __tablename__ = "answers"

    petition_id = Column(Integer, ForeignKey("petitions.petition_id"), primary_key=True)
    contents = Column(Text)
    created_at = Column(DateTime(), default=datetime.now(timezone("Asia/Seoul")))

    def __init__(self, petition_id, contents):
        self.petition_id = petition_id
        self.contents = contents
