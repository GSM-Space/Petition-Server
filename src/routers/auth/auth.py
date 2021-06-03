from fastapi import APIRouter, Header, Response, HTTPException
from typing import Optional

from controller.auth import AuthController
from controller.users import UserController

from model.Schema import Token

auth = APIRouter()


@auth.post("/socialmedia", status_code=200)
def socialmedia(req_form: Token.Social):
    # token_result = auth_by_google_token(req_form.token)
    # sub = token_result.get("sub")

    # if sub is None:
    #     raise HTTPException(status_code=401)

    # user = UserController(id=sub).get_user()

    # if not user.email:
    #     user = UserController.register_user(token_result)

    token = AuthController.issue_token({"sub": "111061074090493497044"})
    return {"token": token}
