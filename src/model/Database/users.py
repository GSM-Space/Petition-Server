from sqlalchemy import Table, Column, Integer, String, DateTime, Text, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone
import enum

from .base import Base


class Authority(enum.Enum):
    """
    student: 학생
    teacher: 선생님
    admin: 관리자
    """

    student = 1
    teacher = 2
    admin = 3


class Users(Base):
    __tablename__ = "users"

    std_id = Column(String(32), primary_key=True)
    email = Column(String(255), nullable=False)
    name = Column(String(45), nullable=False)
    authority = Column(Enum(Authority), default=Authority.student)
    my_petitions = relationship("Petitions", backref="users")
    agreed = relationship("Petitions", backref="agreements")

    def __init__(self, std_id, email, name):
        self.std_id = std_id
        self.email = email
        self.name = name
