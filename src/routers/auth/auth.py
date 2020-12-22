from fastapi import APIRouter, Header
from typing import Optional

from controller.users import get_user_info, register_user
from controller.auth import auth_by_token

auth = APIRouter()


@auth.post("/socialmedia")
def socialmedia(authorization: Optional[str] = Header(None)):
    data = auth_by_token(authorization)

    info = None
    if data:
        info = get_user_info(data)
    else:
        info = register_user(data)
    return info
