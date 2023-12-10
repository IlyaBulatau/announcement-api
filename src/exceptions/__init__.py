from fastapi import FastAPI
from src.exceptions.handlers import (
    invalid_input_exception_handler,
    duplicate_object_exception_handler,
)
from src.exceptions.exceptions import InvalidInput, DuplicateObject


def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidInput, invalid_input_exception_handler)
    app.add_exception_handler(DuplicateObject, duplicate_object_exception_handler)
