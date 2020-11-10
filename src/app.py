from fastapi import FastAPI

from routers import test

app = FastAPI()


app.include_router(
    test.router,
    prefix="/api",
    tags=["api"],
    responses={404: {"description" : "Not found"}},
)