from fastapi import APIRouter, Header
from typing import Optional


from .petitions import petitions
from .admin import admin
from .auth import auth

router = APIRouter()


@router.post("/test")
def test():
    return "petition"


router.include_router(
    petitions,
    prefix="/petitions",
    tags=["petitions"],
    responses={404: {"description": "Not found"}},
)

router.include_router(
    auth,
    prefix="/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)

router.include_router(
    admin,
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)
