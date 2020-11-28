from pydantic import BaseModel
from datetime import datetime
from typing import List


class Petition(BaseModel):

    petitioner : str
    title: str
    contents: str
    proposal : str
    agreed : int
    answer : str
    status : int = 1
    created_at: datetime = datetime.now()


class Total_Petition(BaseModel):
    """
    총 청원에 관한 모델
    Petition은 청원들의 리스트
    expiration_Petition은 만료된 청원
    answered_Petition은 답변된 청원
    ongoing_Petitiond은 진행중인 청원
    pending_Petition은 답변 대기중인 청원
    """

    Petition: List[Petition] = None
    expiration_Petition: List[Petition] = None
    answered_Petition: List[Petition] = None
    ongoing_Petition: List[Petition] = None
    pending_Petition: List[Petition] = None

    class Config:
        arbitrary_types_allowed = True
