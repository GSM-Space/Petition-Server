from sqlalchemy import Table, Column, Integer, DateTime, Text, Enum, ForeignKey, String
from sqlalchemy.orm import relationship

from datetime import datetime, timedelta
from pytz import timezone
import enum

from model.Database import Base


class PetitionStatus(enum.Enum):
    """
    ongoing : 진행중인 청원
    pending : 답변 대기중인 청원
    answered : 답변 된 청원
    expired : 기한이 지난 청원
    deleted : 삭제 된 청원
    """

    ongoing = 1
    pending = 2
    answered = 3
    expired = 4
    deleted = 5


class Petitions(Base):
    __tablename__ = "petitions"

    petition_id = Column(Integer, primary_key=True, autoincrement=True)
    petitioner = Column(String(32), ForeignKey("users.std_id"))
    title = Column(Text, nullable=False)
    contents = Column(Text, nullable=False)
    proposal = Column(Text, nullable=False)
    created_at = Column(DateTime(), default=datetime.now(timezone("Asia/Seoul")))
    end_at = Column(
        DateTime(), default=datetime.now(timezone("Asia/Seoul")) + timedelta(days=30)
    )
    status = Column(Enum(PetitionStatus), default=PetitionStatus.ongoing)

    # the_petitioner = relationship("Students", back_populates="my_petitions")

    agreed = relationship("Agreements", back_populates="petition")
    answer = relationship("Answers", back_populates="petition")

    def __init__(self, title, contents, proposal, petitioner):
        self.title = title
        self.contents = contents
        self.proposal = proposal
        self.petitioner = petitioner
