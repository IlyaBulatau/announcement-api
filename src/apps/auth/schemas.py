import uuid
from datetime import datetime
from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str 
    created_on: datetime
    update_on: datetime 

    class Confg:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    username: str 


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str] = None