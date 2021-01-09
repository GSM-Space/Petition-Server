from sqlalchemy import Table, Column, Integer, Text, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from datetime import datetime
from pytz import timezone

from .base import Base


class Answers(Base):
    __tablename__ = "answers"

    petition_id = Column(Integer, ForeignKey("petitions.petition_id"), primary_key=True)
    contents = Column(Text, nullable=False)
    answered_by = Column(String(45), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(timezone("Asia/Seoul")))

    petition = relationship("Petitions", back_populates="answer")

    def __init__(self, petition_id, contents, answered_by):
        self.petition_id = petition_id
        self.contents = contents
        self.answered_by = answered_by
