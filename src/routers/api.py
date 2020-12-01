from fastapi import APIRouter, Depends
from model.Response.petition import CreatePetition
from model.Database.petitions import create_petition as new_petition

router = APIRouter()

@router.post("/test")
def test():
    return "petition"

@router.post("/create/petition")
def create_petition(req_form : CreatePetition):
    #TODO 사용자의 입력값 검증
    return new_petition(req_form)
