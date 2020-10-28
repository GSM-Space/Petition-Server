from pydantic import BaseModel

class account:
    """
    name은 유저 닉네임
    consent는 청원 동의한 것들의 리스트
    """
    name : str
    consent : List[str]

