from fastapi_sqlalchemy import db
from sqlalchemy.sql import func

from model.Schema import Petition
from model.Database.petitions import Petitions
from model.Database.agreements import Agreements


def new_petition(data: Petition.Create):
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


def get_petition_list(status: str, page: int):

    con = db.session
    petition_list = (
        con.query(
            Petitions.petition_id,
            Petitions.title,
            func.count("std_id").label("agreed"),
            Petitions.end_at,
        )
        .group_by(Petitions.petition_id)
        .all()
    )
    # petition_list = con.query(Petitions).filter(Petitions.status == status).all()
    max_page = len(petition_list) // 5 + 1
    return {"petitions": petition_list, "max_page": max_page}
