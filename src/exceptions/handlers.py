from fastapi.requests import Request
from fastapi.responses import JSONResponse

from src.exceptions.exceptions import InvalidInput, DuplicateObject


async def invalid_input_exception_handler(request: Request, exc: InvalidInput):
    return JSONResponse(
        status_code=422,
        content={"Error": f"Invalid field input"},
    )


async def duplicate_object_exception_handler(request: Request, exc: DuplicateObject):
    return JSONResponse(
        status_code=422, content={"Error": "An object with this data already exists"}
    )
