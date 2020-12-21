import requests
from fastapi_sqlalchemy import db

from model.Database.petitions import Petitions
from model.Database.users import Users
from controller.auth import auth_account


def rne(id_token: str):
    data = auth_account(id_token)
    con = db.session
    try:
        check = con.query(Users).filter(Users.std_id == data["sub"]).first()
    except (KeyError):
        return {"error": "만료된 토큰입니다."}
    if not check:
        account = Users(std_id=data["sub"], email=data["email"], name=data["name"])
        con.add(account)
        con.commit()
        con.refresh(account)
        return {"information": {"email": data["email"], "name": data["name"]}}

    return {"information": {"email": check.email, "name": check.name}}
