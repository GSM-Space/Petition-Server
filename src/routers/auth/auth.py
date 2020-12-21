from fastapi import APIRouter, Header
from typing import Optional

from controller.student import get_user_info

auth = APIRouter()


@auth.post("/socialmedia")
def socialmedia(authorization: Optional[str] = Header(None)):
    return get_user_info(authorization)
