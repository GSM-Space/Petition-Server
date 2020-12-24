from fastapi import APIRouter, Header
from typing import Optional

from controller.users import UserController


auth = APIRouter()


@auth.post("/socialmedia")
def socialmedia(authorization: Optional[str] = Header(None)):
    user = UserController(id_token=authorization)
    info = user.get_user_info()
    return info
