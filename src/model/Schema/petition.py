from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Petition:
    class Base(BaseModel):
        title: str

    class Create(Base):
        petitioner: int
        contents: str
        proposal: str

        class Config:
            orm_mode = True

    class Preview(Base):
        id: Optional[int]
        status: int
        agreed: int
        end_at: datetime

    class View(Preview):
        created_at: datetime
        contents: str
        proposal: str
        agreeable: Optional[bool]
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
