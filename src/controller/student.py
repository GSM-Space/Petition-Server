import requests
from fastapi_sqlalchemy import db

from model.Database.students import Students
from controller.auth import auth_account


def rne(id_token: str):
    data = auth_account(id_token)
    con = db.session
    print(data)
    check = con.query(Students).filter(Students.std_id == data["sub"]).first()

    if not check:
        account = Students(
            std_id=data["sub"],
            email=data["email"],
            name=data["name"].encode("utf-8"),
        )
        con.add(account)
        con.commit()
        con.refresh(account)
        return {"account": account}

    return id_token