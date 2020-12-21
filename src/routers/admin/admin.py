from fastapi import APIRouter, Header
from typing import Optional

from model.Schema import Answer

admin = APIRouter()


@admin.post("/answers/{id}")
def register_answers(
    id: int, req_form: Answer, authorization: Optional[str] = Header(None)
):
    # TODO 청원 답변 등록 기능 구현
    return "answers"


@admin.put("answers/{id}")
def modify_answers(
    id: int, req_form: Answer, authorization: Optional[str] = Header(None)
):
    # TODO 청원 답변 수정 기능 구현
    return "answers"
