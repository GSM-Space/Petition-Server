from pydantic import BaseModel
from datetime import datetime
from typing import List

class Petition(BaseModel):

    title : str

class CreatePetition(Petition):

    petitioner : int
    contents: str
    proposal : str

    class Config:
        orm_mode = True

class ListPetitions(Petition):

    end_at : datetime
    title : str
    agreed : int
    status : int

class ViewPetition(ListPetitions):

    contents : str
    proposal : str
    created_at : datetime
    answer : str
