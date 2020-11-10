from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test():
    return {"name" : "sunrabbit123"}
