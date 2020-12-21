from fastapi_sqlalchemy import db
import requests


def auth_account(id_token: str):
    auth_url = "https://oauth2.googleapis.com/tokeninfo?id_token="
    res = requests.get(f"{auth_url}{id_token}")
    return res.json()
