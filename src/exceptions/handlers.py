from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.exceptions.exceptions import InvalidInput

async def invalid_input_exception_handler(request: Request, exc: InvalidInput):
    return JSONResponse(
        status_code=422,
        content={"Error": f"Invalid field input"},
    )