from pydantic import BaseModel
from datetime import datetime
from typing import List

class Petition(BaseModel):
    """
    title은 제목
    content는 내용
    solution는 해결방안
    consent는 동의 수, 참여자 수
    """

    title: str
    content: str
    solution: str
    consent: int
    created_At: datetime = datetime.now()


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



