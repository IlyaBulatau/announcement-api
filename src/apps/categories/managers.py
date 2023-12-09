from sqlalchemy import delete, select
from fastapi_users.models import ID
from sqlalchemy.exc import DBAPIError

from src.database.manager import RepositoryManager
from src.database.models import Comment
from src.exceptions.exceptions import InvalidInput
from src.settings import logger


class CategoryRepositoryManager(RepositoryManager):
    pass


class CommentRepositoryManager(RepositoryManager):
    async def get_detail(self, comment_id: ID) -> Comment | None:
        query = select(Comment).filter(Comment.id == comment_id)

        try:
            result = await self.session.execute(query)
        except DBAPIError as error:
            logger.info(error)
            raise InvalidInput(error)
        
        return result.scalar()

    async def delete(self, comment_id: ID) -> None:
        query = delete(Comment).filter(Comment.id == comment_id)
        await self.session.execute(query)
