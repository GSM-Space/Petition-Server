from fastapi import APIRouter, Header
from typing import Optional

from controller.users import get_user_info, register_user

auth = APIRouter()


@auth.post("/socialmedia")
def socialmedia(authorization: Optional[str] = Header(None)):
    info = get_user_info(authorization)
    if info is None:
        info = register_user(authorization)
    return info