from fastapi import APIRouter

from model.Schema.petition import CreatePetition
from model.Database.petitions import create_petition as new_petition

petitions = APIRouter()

@petitions.post("/")
def create_petition(req_form : CreatePetition):
    #TODO 사용자의 입력값 검증
    return new_petition(req_form)
