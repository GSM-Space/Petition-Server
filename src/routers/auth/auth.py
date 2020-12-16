from fastapi import APIRouter, Header
from typing import Optional

from controller.student import rne

auth = APIRouter()

@auth.post("/auth/socialmedia")
def socialmedia(authorization : Optional[str] = Header(None)):
    return rne(authorization)

