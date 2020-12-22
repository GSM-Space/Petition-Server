import requests
from fastapi_sqlalchemy import db

from model.Database.petitions import Petitions
from model.Database.users import Users
from controller.auth import auth_by_token


def get_user_info(data):
    con = db.session
    try:
        check = con.query(Users).filter(Users.std_id == data["sub"]).first()
    except (KeyError):
        return {"error": "만료된 토큰입니다."}
    try:
        return {"information": {"email": check.email, "name": check.name}}
    except Exception as e:
        # 에러는 나올텐데, 무슨에러일지를 몰라서 우선적으로 에러 출력하게 Exception으로 적어놓았어요
        print(e)
        return None


def register_user(data):
    account = Users(std_id=data["sub"], email=data["email"], name=data["name"])
    con.add(account)
    con.commit()
    con.refresh(account)
    return {"information": {"email": data["email"], "name": data["name"]}}