import configparser

config = configparser.ConfigParser()
config.read("config.ini")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from middlewares.DBSession import DBSession
from routers import api


app = FastAPI()

app.add_middleware(DBSession, db_url=config.get("default", "DB_URL"))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # TODO 추후 정확히 메서드 입력
    allow_headers=["*"],
)

app.include_router(
    api.router,
    prefix="/api",
    responses={404: {"description": "Not found"}},
)
