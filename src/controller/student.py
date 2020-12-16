import requests
from fastapi_sqlalchemy import db

from model.Database.students import Students
def rne(id_token : str):
    auth_url = 'https://oauth2.googleapis.com/tokeninfo?id_token='
    res = requests.get(f"{auth_url}{id_token}")
    data = res.json

    con = db.session
    check = con.query(Students).filter(Students.std_id == data['sub'])
    
    if not check:
        account = Students(
            std_id = data['sub'],
            email = data['email'],
            name = data['name']
        )
        return account
    

    return id_token