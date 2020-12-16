from fastapi import APIRouter

admin = APIRouter()


@admin.post("/answers/{id}")
def register_answers(id: int):
    # TODO 청원 답변 등록 기능 구현
    return "answers"


@admin.put("answers/{id}")
def modify_answers(id: int):
    # TODO 청원 답변 수정 기능 구현
    return "answers"
