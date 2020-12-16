from fastapi import APIRouter, Response, status

from model.Schema.petition import CreatePetition, ViewPetition

from controller.petitions import counting_petition, new_petition, consent_petition


petitions = APIRouter()


@petitions.get("/count")
def count_petition():
    return counting_petition()


@petitions.get("")
def list_petitions(status: str = "ongoing", page: int = 1):
    # TODO 사용자 입력값 검증
    # TODO 청원 목록 불러오기 구현
    # TODO status를 잘못 입력시 400 return

    return "list"


@petitions.get("/search")
def search_petitons(q: str, page: int = 1):
    # TODO 청원 검색 기능 구현
    # TODO 사용자 입력값 검증
    return "search"


@petitions.post("")
def create_petition(
    req_form: CreatePetition, authorization: Optional[str] = Header(None)
):
    # TODO 사용자의 입력값 검증
    return new_petition(req_form)


@petitions.get("/{id}", response_model=ViewPetition)
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
    result = consent_petition(id)
    if result == 200:
        response.status_code = status.HTTP_200_OK
    elif result == 400:
        response.status_code = status.HTTP_400_BAD_REQUEST
    elif result == 404:
        response.status_code = status.HTTP_404_NOT_FOUND

    return "dtd"
