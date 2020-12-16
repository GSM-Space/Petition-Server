from fastapi_sqlalchemy import db

from model import Schema
from model.Database.petitions import Petitions
from model.Database.agreements import Agreements


def new_petition(data: Schema.CreatePetition):
    db_petition = Petitions(
        title=data.title,
        contents=data.contents,
        proposal=data.proposal,
        petitioner=str(data.petitioner),
    )
    con = db.session
    con.add(db_petition)
    con.commit()
    con.refresh(db_petition)
    return {"id": db_petition.petition_id}


def counting_petition():
    con = db.session

    total = con.query(Petitions).count()
    answered = con.query(Petitions).filter(Petitions.status == "answered").count()
    pending = con.query(Petitions).filter(Petitions.status == "pending").count()

    return {"total": total, "answered": answered, "pending": pending}


def consent_petition(id: int):
    con = db.session

    result = con.query(Agreements).filter(Agreements.petition_id == id).first()

    if result:
        # 유저 아이디또한 존재하면 return 400
        # 없다면 return 200
        return 400
    return 404
