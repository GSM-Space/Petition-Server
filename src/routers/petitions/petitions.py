from fastapi import APIRouter, Response, HTTPException
from fastapi import status as res_status
from fastapi.param_functions import Depends
from model.Database.petitions import PetitionStatus


from model.Schema import Petition, PetitionResponse
from model.Schema.user import User

from controller.petitions import PetitionController
from controller.users import UserController
from controller.auth import auth_user, login_required

petitions = APIRouter()


@petitions.get("/count", response_model=PetitionResponse.Count)
def count_petition():
    return PetitionController.count_petitions()


@petitions.get("", status_code=200)
def list_petitions(status: str = "ongoing", page: int = 1):
    if not status in ["ongoing", "pending", "answered", "expired"]:
        raise HTTPException(400, "Bad Request")
    return PetitionController.get_petitions(status=status, page=page)


@petitions.get("/search", response_model=PetitionResponse.List)
def search_petitons(q: str = "", page: int = 1):
    return PetitionController.search_petitions(q=q, page=page)


@petitions.post("", response_model=PetitionResponse.Id)
def create_petition(
    req_form: Petition.Create, current_user: User = Depends(login_required)
):
    petition = req_form.dict()
    petition.update(petitioner=current_user.id)
    return PetitionController(**petition).create()


@petitions.get("/{id}", response_model=Petition.View)
def load_petition(id: int, current_user: User = Depends(auth_user)):
    petition: Petition.View = PetitionController.load(id=id, user=current_user)
    if petition is None:
        raise HTTPException(404, "Not Found")

    if current_user:
        agreed = PetitionController.is_agreed(id, current_user)
        petition.agreeable = "agreed" if agreed else "not_agreed"

    return petition


@petitions.delete("/{id}", status_code=204)
def delete_petition(id: int, current_user: User = Depends(login_required)):
    petition = PetitionController.delete(id, current_user)

    if petition is None:
        raise HTTPException(404, "Not Found")
    if petition.status != PetitionStatus.deleted:
        raise HTTPException(403, "Forbidden")

    return Response(status_code=204)


@petitions.post("/{id}", status_code=200)
def agree_petition(id: int, current_user: User = Depends(login_required)):
    result = PetitionController.consent(id, current_user)

    if result is None:
        raise HTTPException(404, "Not Found")

    return Response(status_code=200)
