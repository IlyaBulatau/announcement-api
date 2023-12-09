from fastapi import FastAPI
from src.exceptions.handlers import invalid_input_exception_handler
from src.exceptions.exceptions import InvalidInput

def setup_exception_handlers(app: FastAPI):
    app.add_exception_handler(InvalidInput, invalid_input_exception_handler)