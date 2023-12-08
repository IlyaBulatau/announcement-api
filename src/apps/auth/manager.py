import uuid
from typing import Union

from fastapi_users import models, schemas, exceptions as exc
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, UUIDIDMixin
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.models import User
from src.apps.auth import get_user_db
from src.apps.auth.schemas import UserCreate


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    
    async def create(self, user_create: schemas.UC, safe: bool = False, request: Request | None = None) -> models.UP:
        await self.validate_username(user_create.username)
        return await super().create(user_create, safe, request)
    
    async def validate_username(self, username: str):
        if await self.user_is_exists(self.user_db.session, username):
            raise exc.UserAlreadyExists()
        

    async def validate_password(
        self,
        password: str,
        user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise exc.InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise exc.InvalidPasswordException(
                reason="Password should not contain e-mail"
            )

    async def user_is_exists(self, session: AsyncSession, username: str) -> bool:
        query = select(User).filter(User.username==username)
        resul = await session.execute(query)
        return resul.scalar()

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)