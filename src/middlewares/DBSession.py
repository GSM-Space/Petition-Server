from sqlalchemy import create_engine
from fastapi_sqlalchemy import DBSessionMiddleware

from model.Database import Base


class DBSession(DBSessionMiddleware):
    def __init__(self, db_url=None, custom_engine=None, *args, **kwargs):
        if not db_url and not custom_engine:
            raise ValueError("You need to pass a db_url or a custom_engine parameter.")
        if not custom_engine:
            custom_engine = create_engine(db_url)

        Base.metadata.create_all(custom_engine)
        super().__init__(custom_engine=custom_engine, *args, **kwargs)
