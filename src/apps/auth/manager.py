import uuid
from typing import Optional

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin

from src.database.models import User
from src.apps.auth import get_user_db


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    pass
    

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)