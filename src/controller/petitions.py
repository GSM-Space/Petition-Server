from sqlalchemy import desc
from fastapi_sqlalchemy import db
from sqlalchemy.sql import func

from datetime import datetime

from model.Schema import Petition, Answer
from model.Database import Petitions, Agreements, PetitionStatus


class PetitionController:
    def __init__(self):
        pass

    @staticmethod
    def create(data: Petition.Create):
        db_petition = Petitions(**data.dict())
        con = db.session
        con.add(db_petition)
        con.commit()
        con.refresh(db_petition)
        return {"id": db_petition.petition_id}

    @staticmethod
    def consent(petition_id, user_id):
        con = db.session

        result = (
            con.query(Petitions).filter(Petitions.petition_id == petition_id).first()
        )
        if not result:
            return 404
        elif con.query(Agreements).filter(Agreements.petition_id == self.id).first():
            return 400

        agreement = Agreements(user_id, self.id)
        con.add(agreement)
        con.commit()
        con.refresh(agreement)

        return 200

    @staticmethod
    def load(id: int):
        con = db.session

        result = (
            con.query(Petitions, func.count("agreed").label("agreed"))
            .filter(Petitions.petition_id == id)
            .first()
        )

        if result[0] is None:
            return None

        petition = Petition.View(**result[0].__dict__, agreed=result[1])

        return petition

    @staticmethod
    def is_agreed(petition_id: int, user_id: int):
        con = db.session

        result = (
            con.query(Agreements)
            .filter(Agreements.petition_id == petition_id)
            .filter(Agreements.std_id == user_id)
            .first()
        )

        return bool(result)

    def delete(self):
        con = db.session
        petition = con.query(Petitions).filter(Petitions.petition_id == self.id).first()

        try:
            if petition.status == PetitionStatus.deleted:
                res_status = 404
            elif petition.petitioner == self.petitioner:
                res_status = 204
                petition.status = PetitionStatus.deleted
                con.commit()
            elif petition:
                res_status = 403
        except AttributeError:
            res_status = 404

        return res_status

    @staticmethod
    def count_petitions():
        con = db.session

        total = con.query(Petitions).count()
        answered = con.query(Petitions).filter(Petitions.status == "answered").count()
        pending = con.query(Petitions).filter(Petitions.status == "pending").count()

        return {"total": total, "answered": answered, "pending": pending}

    @staticmethod
    def search_petitions(q: str, page: int):
        con = db.session
        min_limit = (page - 1) * 5
        searched = (
            con.query(
                Petitions.petition_id.label("petition_id"),
                Petitions.title.label("title"),
                func.count("agreed").label("agreed"),
                Petitions.end_at.label("end_at"),
                Petitions.status.label("status"),
            )
            .filter(Petitions.title.like(f"%{q}%"))
            .group_by(Petitions.petition_id)
            .order_by(desc(Petitions.petition_id))
            .all()
        )
        label = ["petition_id", "title", "agreed", "end_at", "status"]
        petition_list = [
            {key: value for (key, value) in zip(label, row)} for row in searched
        ]
        max_page = ((len(petition_list) - 1) // 5) + 1
        return {
            "petitions": petition_list[min_limit : min_limit + 5],
            "max_page": max_page,
        }

    @staticmethod
    def get_petitions(status: str, page: int):
        con = db.session
        min_limit = (page - 1) * 5
        get_list = (
            con.query(
                Petitions.petition_id.label("petition_id"),
                Petitions.title.label("title"),
                func.count("agreed").label("agreed"),
                Petitions.end_at.label("end_at"),
            )
            .filter(Petitions.status == status)
            .group_by(Petitions.petition_id)
            .order_by(desc(Petitions.petition_id))
            .all()
        )

        label = ["petition_id", "title", "agreed", "end_at"]
        petition_list = [
            {key: value for (key, value) in zip(label, row)} for row in get_list
        ]
        max_page = (len(petition_list) - 1) // 5 + 1

        return {"petitions": petition_list, "max_page": max_page}

    def presence_petition(self) -> bool:
        con = db.session

        get_petition = (
            con.query(Petitions)
            .filter(Petitions.petition_id == self.petition_id)
            .first()
        )
        return get_petition

    def register_answers(self, req_form: Answer):
        con = db.session

        answer = Answers(
            petition_id=self.id,
            contents=req_form.contents,
            answered_by=req_form.answered_by,
        )

        con = db.session
        con.add(answer)
        con.commit()
        con.refresh(answer)
