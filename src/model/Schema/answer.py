from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class Answer(BaseModel):
    contents: str
    answered_by: str
