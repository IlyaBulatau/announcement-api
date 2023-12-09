from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from src.database.models import User
from src.database.connection import get_async_session
from src.apps.auth.schemas import UserUpdate, UserCreate


class UserRepositoryManager:

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
    
    async def set_permission(self, user_schema: UserUpdate) -> UserCreate | None:    
        query = (
            update(User)
            .filter(User.username==user_schema.username)
            .values(is_superuser=True)
            .returning(User))
        
        result = await self.session.execute(query)
        return result.scalar()
