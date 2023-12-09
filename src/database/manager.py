from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from abc import ABC

from src.database.connection import get_async_session


class RepositoryManager(ABC):

    def __init__(self, session: AsyncSession = Depends(get_async_session)):
        self.session = session
