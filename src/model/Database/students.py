from sqlalchemy import Table, Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from pytz import timezone

from .base import Base


class Students(Base):
    __tablename__ = "students"

    std_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), nullable=False)
    name = Column(String(45), nullable=False)
    is_admin = Column(Boolean, default=False)
    my_petitions = relationship("Petitions", backref="petitioner")
    agreed = relationship("Petitions", backref="consent_student")

    def __init__(self, email, password, name):
        self.email = email
        self.password = self.hash_password(password)
        self.std_number = std_number
        self.name = name
