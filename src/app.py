from fastapi import FastAPI
import configparser

from middlewares.DBSession import DBSession
from routers import test

config = configparser.ConfigParser()
config.read("config.ini")

app = FastAPI()
app.add_middleware(DBSession, db_url=config.get("default", "DB_URL"))

app.include_router(
    test.router,
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)
