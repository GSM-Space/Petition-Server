from sqlalchemy import Table, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone

from .base import Base


class Students(Base):
    __tablename__ = "students"

    std_id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False)
    name = Column(String(45), nullable=False)
    my_petitions = relationship("Petitions", backref="students")
    agreed = relationship("Petitions", backref="agreements")

    def __init__(self, std_id, email, password, name):
        self.std_id = std_id
        self.email = email
        self.password = self.hash_password(password)
        self.std_number = std_number
        self.name = name

    def hash_password(self, password):
        # TODO: 비밀번호 해쉬
        return password
