from typing import Optional
from fastapi.exceptions import HTTPException
from fastapi.params import Header
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
from jose import jwt, JWTError

from google.oauth2 import id_token
from google.auth.transport import requests

from app import config
from controller.users import UserController


TOKEN_TTL = config.get("default", "TOKEN_TTL")
JWT_SECRET = config.get("default", "JWT_SECRET")
JWT_ALGORITHM = config.get("default", "JWT_ALGORITHM")
CLIENT_ID = config.get("default", "GOOGLE_OAUTH_CLIENT_ID")


def auth_by_google_token(token: str):
    try:
        info = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)
    except ValueError:
        return {"error": "Invalid Token"}
    return info


class AuthController:
    @staticmethod
    def issue_token(data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=int(TOKEN_TTL))
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return encoded_jwt

    @staticmethod
    def decode_token(token: str):
        payload = jwt.decode(token, JWT_SECRET, algorithms=JWT_ALGORITHM)
        return payload


def auth_user(authorization: str = Header(None)):
    if not authorization:
        return None

    try:
        payload = AuthController.decode_token(authorization)
        user_email = payload.get("sub", None)
    except JWTError:
        return None

    user = UserController().get_user(email=user_email)

    return user


def login_required(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(401, detail="로그인을 해주세요")

    user = auth_user(authorization)

    if user is None:
        raise HTTPException(401, detail="로그인을 해주세요")
