import requests
from fastapi_sqlalchemy import db

from typing import List, Optional

from model.Database.petitions import Petitions
from model.Database.users import Users, Authority

from controller.auth import auth_by_token


class UserController:
    def __init__(
        self,
        id: str = None,
        email: str = None,
        name: str = None,
        authority: str = None,
        my_petitions: Optional[List[Petitions]] = None,
        agreed: int = None,
        id_token: str = None,
    ):
        self.id = id
        self.email = email
        self.name = name
        self.authority = authority
        self.my_petitions = my_petitions
        self.agreed = agreed
        self.data = auth_by_token(id_token)

    def get_user_info(self):
        con = db.session
        try:
            check = con.query(Users).filter(Users.std_id == self.data["sub"]).first()
        except (KeyError):
            return {"error": "만료된 토큰입니다."}
        try:
            self.id = check.std_id
            return {"information": {"email": check.email, "name": check.name}}
        except AttributeError:
            return UserController.register_user(self.data)

    @staticmethod
    def register_user(data):
        con = db.session
        account = Users(
            std_id=data["sub"],
            email=data["email"],
            name=data["name"],
        )
        con.add(account)
        con.commit()
        con.refresh(account)
        return {"information": {"email": data["email"], "name": data["name"]}}

    def auth_admin(self):
        con = db.session
        try:
            check = con.query(Users).filter(Users.std_id == self.data["sub"]).first()
            return check.authority
        except (KeyError):
            return {"error": "만료된 토큰입니다."}
