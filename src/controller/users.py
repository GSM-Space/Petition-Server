import requests
from fastapi_sqlalchemy import db

from model.Database.petitions import Petitions
from model.Database.users import Users
from controller.auth import auth_by_token


def get_user_info(id_token: str):
    data = auth_by_token(id_token)
    con = db.session
    try:
        check = con.query(Users).filter(Users.std_id == data["sub"]).first()
    except (KeyError):
        return {"error": "만료된 토큰입니다."}
    try:
        return {"information": {"email": check.email, "name": check.name}}
    except (Exception e):
        return None
        

def register_user(id_token: str):
    account = Users(std_id=data["sub"], email=data["email"], name=data["name"])
    con.add(account)
    con.commit()
    con.refresh(account)
    return {"information": {"email": data["email"], "name": data["name"]}}