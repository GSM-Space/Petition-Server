from fastapi import APIRouter, HTTPException

from controller.auth import AuthController, auth_by_google_token
from controller.users import UserController

from model.Schema import Token
from model.Schema.user import User

auth = APIRouter()


@auth.post("/socialmedia", status_code=200)
def socialmedia(req_form: Token.Social):
    token_result = auth_by_google_token(req_form.token)
    sub = token_result.get("sub")

    if sub is None:
        raise HTTPException(status_code=401)

    user = UserController(id=sub).get_user()

    if not user.email:
        user: User = UserController.register_user(token_result)

    token = AuthController.issue_token({"sub": user.email})
    return {"token": token}
