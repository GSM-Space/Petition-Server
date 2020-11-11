from sqlalchemy import Table, Column, Integer, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from pytz import timezone
import enum

from .base import Base


class PetitionStatus(enum.Enum):
    ongoing = 1
    pending = 2
    answered = 3
    expired = 4
    deleted = 5


class Petitions(Base):
    __tablename__ = "petitions"

    petition_id = Column(Integer, primary_key=True)
    petitioner = Column(Integer, ForeignKey("students.std_id"))
    title = Column(Text, nullable=False)
    contents = Column(Text, nullable=False)
    proposal = Column(Text, nullable=False)
    created_at = Column(DateTime(), default=datetime.now(timezone("Asia/Seoul")))
    end_at = Column(
        DateTime(), default=datetime.now(timezone("Asia/Seoul")) + timedelta(days=30)
    )
    status = Column(Enum(PetitionStatus), default=1)
    agreed = relationship("Petitions", backref="agreements")
    answer = relationship("Petitions", backref="answers")

    def __init__(self, title, contents, proposal, petitioner):
        self.title = title
        self.contents = contents
        self.proposal = proposal
        self.petitioner = petitioner
