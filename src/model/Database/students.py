from sqlalchemy import Table, Column, BigInteger, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone

from .base import Base


class Students(Base):
    __tablename__ = "students"

    std_id = Column(String(32), primary_key=True)
    email = Column(String(255), nullable=False)
    name = Column(String(45), nullable=False)
    my_petitions = relationship("Petitions", backref="students")
    agreed = relationship("Petitions", backref="agreements")

    def __init__(self, std_id, email, name):
        self.std_id = std_id
        self.email = email
        self.name = name
