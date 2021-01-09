from fastapi import APIRouter, Header
from typing import Optional

from model.Schema import Answer
from controller.users import UserController
from controller.petitions import PetitionController

admin = APIRouter()


def check_admin(func):
    def wrapper(id: int, req_form: Answer, authorization: Optional[str] = Header(None)):
        result = UserController(id_token=authorzation).auth_admin()
        petition_presence = PetitionController(id=id).presence_petition()
        if result == "admin" and petition_presence:
            response.status_code = res_status.HTTP_200_OK
            return func(id=id, req_form=req_form, authorization=authorization)
        response.status_code = res_status.HTTP_404_NOT_FOUND
        return result

    return wrapper


@admin.post("/answers/{id}")
@check_admin
def register_answers(
    id: int, req_form: Answer, authorization: Optional[str] = Header(None)
):
    # TODO 청원 답변 등록 기능 구현
    PetitionController(id=id).register_answers(req_form=req_form)
    return "answers"


@admin.put("answers/{id}")
@check_admin
def modify_answers(
    id: int, req_form: Answer, authorization: Optional[str] = Header(None)
):
    # TODO 청원 답변 수정 기능 구현
    return "answers"
