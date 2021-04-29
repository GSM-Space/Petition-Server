from fastapi import APIRouter, Header, Request, Response
from typing import Optional

from controller.users import UserController


auth = APIRouter()


@auth.post("/socialmedia")
def socialmedia(response: Response, authorization: Optional[str] = Header(None)):
    user = UserController(id_token=authorization)
    info = user.get_user_info()
    if "error" in info:
        response.status_code = 400
    return info
