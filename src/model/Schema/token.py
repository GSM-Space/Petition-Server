from pydantic import BaseModel


class Token:
    class Social(BaseModel):
        token: str
