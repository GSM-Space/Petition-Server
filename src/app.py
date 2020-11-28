from fastapi import FastAPI
import configparser

from middlewares.DBSession import DBSession
from routers import api

config = configparser.ConfigParser()
config.read("config.ini")

app = FastAPI()
app.add_middleware(DBSession, db_url=config.get("default", "DB_URL"))

app.include_router(
    api.router,
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)
