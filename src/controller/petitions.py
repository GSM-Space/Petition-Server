from sqlalchemy import desc
from fastapi_sqlalchemy import db
from sqlalchemy.sql import func

from datetime import datetime

from model.Schema import Petition
from model.Database import Petitions, Agreements, PetitionStatus


class PetitionController:
    def __init__(
        self,
        id: int = None,
        status: int = None,
        petitioner: int = None,
        title: str = None,
        contents: str = None,
        proposal: str = None,
        agreed: int = None,
        created_at: datetime = None,
        end_at: datetime = None,
        agreeable: bool = None,
        answer: str = None,
        answered_at: datetime = None,
        answered_by: str = None,
    ):
        self.id = id
        self.status = status
        self.petitioner = petitioner
        self.title = title
        self.contents = contents
        self.proposal = proposal
        self.agreed = agreed
        self.created_at = created_at
        self.end_at = end_at
        self.agreeable = agreeable
        self.answer = answer
        self.answered_at = answered_at
        self.answered_by = answered_by

    def create(self):
        data = Petition.Create(
            title=self.title,
            contents=self.contents,
            proposal=self.proposal,
            petitioner=self.petitioner,
        )
        db_petition = Petitions(**data.dict())

        con = db.session
        con.add(db_petition)
        con.commit()
        con.refresh(db_petition)
        return {"id": db_petition.petition_id}

    def consent(self):
        con = db.session

        result = con.query(Agreements).filter(Agreements.petition_id == self.id).first()

        if result:
            # 유저 아이디또한 존재하면 return 400
            # 없다면 return 200
            return 400
        return 404

    def load(self):
        con = db.session

        petition = (
            con.query(
                Petitions.created_at,
                Petitions.contents,
                Petitions.end_at,
                Petitions.title,
                Petitions.status,
                Petitions.proposal,
                func.count("agreed").label("agreed"),
                Petitions.petition_id,
            )
            .filter(Petitions.petition_id == self.id)
            .first()
        )

        label = [
            "created_at",
            "contents",
            "end_at",
            "title",
            "status",
            "proposal",
            "agreed",
            "petition_id",
        ]
        petition_list = {key: value for (key, value) in zip(label, petition)}

        return petition_list

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
        answered = con.query(Petitions).filter(Petitions.status == "answered")
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

        return {
            "petitions": petition_list[min_limit : min_limit + 5],
            "max_page": max_page,
        }
