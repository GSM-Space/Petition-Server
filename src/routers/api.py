from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test():
    return {"name" : "sunrabbit123"}

@router.post("/create")
async def create_petition():
    