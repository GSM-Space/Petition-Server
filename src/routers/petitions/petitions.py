from fastapi import APIRouter, Response, status, Header
from typing import List, Optional

from model.Schema import Petition, PetitionResponse

from controller.petitions import PetitionController


petitions = APIRouter()


@petitions.get("/count", response_model=PetitionResponse.Count)
def count_petition():
    return PetitionController.count_petitions()


@petitions.get("", response_model=PetitionResponse.List)
def list_petitions(status: str = "ongoing", page: int = 1):
    # TODO 사용자 입력값 검증
    # TODO 청원 목록 불러오기 구현
    # TODO status를 잘못 입력시 400 return

    return "list"


@petitions.get("/search", response_model=PetitionResponse.List)
def search_petitons(q: str, page: int = 1):
    # TODO 청원 검색 기능 구현
    # TODO 사용자 입력값 검증
    return "search"


@petitions.post("", response_model=PetitionResponse.Id)
def create_petition(
    req_form: Petition.Create, authorization: Optional[str] = Header(None)
):
    # TODO 사용자의 입력값 검증
    return PetitionController(**req_form.dict()).create()


@petitions.get("/{id}", response_model=Petition.View)
def load_petition(id: int):
    # TODO 200은 성공적 반환, 값이 없을 경우 404 반환
    return "load"


@petitions.delete("/{id}")
def delete_petition(id: int, authorization: Optional[str] = Header(None)):
    # TODO 사용자 권한 인증
    # 청원 삭제 기능 구현
    # 204 -> 이미 삭제 된 청원, 403 -> 삭제 권한 없음, 404 -> 없는 청원
    return "delete"


@petitions.post("/{id}")
def agree_petition(
    id: int, response: Response, authorization: Optional[str] = Header(None)
):
    # TODO 사용자 권한 인증
    # 200 -> 성공, 400 -> 이미 동의한 청원, 404 -> 존재하지 않는 청원
    result = PetitionController(id=id).consent()

    if result == 200:
        response.status_code = status.HTTP_200_OK
    elif result == 400:
        response.status_code = status.HTTP_400_BAD_REQUEST
    elif result == 404:
        response.status_code = status.HTTP_404_NOT_FOUND

    return "dtd"
