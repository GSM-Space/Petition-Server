from sqlalchemy import Table, Column, Integer, String, DateTime
from datetime import datetime
from pytz import timezone

from .base import Base


class Students(Base):
    __tablename__ = "students"

    std_id = Column(Integer, primary_key=True, auto_increment=True)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    std_grade = Column(Integer, nullable=False)
    std_class = Column(Integer, nullable=False)
    std_number = Column(Integer, nullable=False)
    name = Column(String(45), nullable=False)

    def __init__(self, email, password, std_grade, std_class, std_number, name):
        self.email = email
        self.password = self.hash_password(password)
        self.std_grade = std_grade
        self.std_class = std_class
        self.std_number = std_number
        self.name = name

    def hash_password(self, password):
        # TODO: 비밀번호 해쉬
        return password
