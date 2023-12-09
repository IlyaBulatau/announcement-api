from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get(
    "/",
    response_description="Return operation status",
    summary="Get healthcheck status"
    )
async def healthcheck():
    """
    Healthcheck Endpoint
    """
    return JSONResponse(
        content={"Status": "OK"},
        status_code=200
        )
