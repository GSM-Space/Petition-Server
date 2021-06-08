from enum import Enum
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from model.Database.petitions import PetitionStatus


class Agreeable(Enum):
    login_required = "login_required"
    not_agreed = "not_agreed"
    agreed = "agreed"


class Petition:
    class Base(BaseModel):
        title: str

    class Create(Base):
        petitioner: Optional[str]
        contents: str
        proposal: str

        class Config:
            orm_mode = True

    class Preview(Base):
        petition_id: Optional[int]
        status: PetitionStatus
        agreed: int
        end_at: datetime

    class View(Preview):
        created_at: datetime
        contents: str
        proposal: str
        agreeable: Optional[Agreeable] = "login_required"
        answer: Optional[str]
        answered_at: Optional[datetime]
        answered_by: Optional[str]


class PetitionResponse:
    class Id(BaseModel):
        id: int

    class Count(BaseModel):
        total: int
        answered: int
        pending: int

    class List(BaseModel):
        petitions: List[Petition.Preview]
        max_page: int
