import requests
from fastapi_sqlalchemy import db

from typing import List, Optional

from model.Database.petitions import Petitions
from model.Database.users import Users, Authority
from model.Schema.user import User


class UserController:
    def __init__(self):
        pass

    @staticmethod
    def get_user(user_id: int = None, email: str = None):
        con = db.session
        queried_user = (
            con.query(Users)
            .filter((Users.std_id == user_id) | (Users.email == email))
            .first()
        )
        user = (
            User(id=queried_user.std_id, **queried_user.__dict__)
            if queried_user
            else None
        )
        return user

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
