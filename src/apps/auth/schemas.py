import uuid
from datetime import datetime

from pydantic import EmailStr
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str
    created_on: datetime
    update_on: datetime

    class Confg:
        orm_mode = True


class UserCreate(schemas.CreateUpdateDictModel):
    username: str
    email: EmailStr
    password: str
