from fastapi import APIRouter


router = APIRouter()

@router.get("/")
async def healthcheck():
    return {"Status": "OK"}

