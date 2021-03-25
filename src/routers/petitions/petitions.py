from fastapi import APIRouter, Response, Header
from fastapi import status as res_status
from typing import Optional

from http import HTTPStatus

from model.Schema import Petition, PetitionResponse

from controller.petitions import PetitionController
from controller.auth import auth_by_token


petitions = APIRouter()
status_dict = {
    "200": res_status.HTTP_200_OK,
    "204": res_status.HTTP_204_NO_CONTENT,
    "400": res_status.HTTP_400_BAD_REQUEST,
    "403": res_status.HTTP_403_FORBIDDEN,
    "404": res_status.HTTP_404_NOT_FOUND,
}


@petitions.get("/count", response_model=PetitionResponse.Count)
def count_petition():
    return PetitionController.count_petitions()


@petitions.get("", status_code=200)
def list_petitions(response: Response, status: str = "ongoing", page: int = 1):
    if not status in ["ongoing", "pending", "answered", "expired", "deleted"]:
        response.status_code = status_dict["404"]
        return {"description": "Invalid status value"}
    return PetitionController.get_petitions(status=status, page=page)


@petitions.get("/search", response_model=PetitionResponse.List)
def search_petitons(q: str = "", page: int = 1):
    return PetitionController.search_petitions(q=q, page=page)


@petitions.post("", response_model=PetitionResponse.Id)
def create_petition(
    req_form: Petition.Create, authorization: Optional[str] = Header(None)
):
    # XSS, 필터의 경우 리액트에서 적용함
    # SQLI의 경우 Test 필요
    return PetitionController(**req_form.dict()).create()


@petitions.get("/{id}", response_model=Petition.View)
def load_petition(id: int):
    # TODO 200은 성공적 반환, 값이 없을 경우 404 반환
    petitions = PetitionController(id=id).load()
    if petitions:
        response.status_code = status_dict["200"]
    else:
        response.status_code = status_dict["404"]

    return petitions


@petitions.delete("/{id}")
def delete_petition(
    id: int, response: Response, authorization: Optional[str] = Header(None)
):
    # TODO 사용자 권한 인증
    # publisher = auth_by_token(authorization)["sub"]
    status = PetitionController(id=id, petitioner="113799700035273671200").delete()
    response.status_code = status_dict[str(status)]
    if status == 204:
        return Response(status_code=HTTPStatus.NO_CONTENT.value)
    # 204 -> 이미 삭제 된 청원, 403 -> 삭제 권한 없음, 404 -> 없는 청원


@petitions.post("/{id}")
def agree_petition(
    id: int, response: Response, authorization: Optional[str] = Header(None)
):
    # TODO 사용자 권한 인증
    # 200 -> 성공, 400 -> 이미 동의한 청원, 404 -> 존재하지 않는 청원
    status = PetitionController(id=id).consent()

    response.status_code = status_dict[str(status)]

    return
