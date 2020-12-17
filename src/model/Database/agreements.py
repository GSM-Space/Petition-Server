from sqlalchemy import Table, Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from datetime import datetime
from pytz import timezone

from .base import Base


class Agreements(Base):
    __tablename__ = "agreements"

    std_id = Column(String(32), ForeignKey("users.std_id"), primary_key=True)
    petition_id = Column(Integer, ForeignKey("petitions.petition_id"), primary_key=True)
    created_at = Column(DateTime(), default=datetime.now(timezone("Asia/Seoul")))

    petition = relationship("Petitions", back_populates="agreed")

    def __init__(self, std_id, petition_id):
        self.std_id = std_id
        self.petition_id = petition_id
