from sqlalchemy import select, insert, delete
from fastapi_users.models import ID
from sqlalchemy.exc import DBAPIError, IntegrityError

from src.database.models import Announcement, Category
from src.database.manager import RepositoryManager
from src.apps.announcements.schemas import (
    AnnouncementCreate,
)
from src.exceptions.exceptions import InvalidInput, DuplicateObject
from src.apps.announcements.constances import PAGINATE_OFFSET, PAGINATE_LIMIT
from src.settings import logger


class AnnouncementRepositoryManager(RepositoryManager):
    async def create(
        self, announcement_schema: AnnouncementCreate, user_id: ID
    ) -> tuple[Announcement, Category]:
        announcement = announcement_schema.model_dump()
        category: Category = await self.get_or_create_category(
            announcement.pop("category")
        )
        query = (
            insert(Announcement)
            .values(
                title=announcement.get("title"),
                content=announcement.get("content"),
                category_id=category.id,
                user_id=user_id,
            )
            .returning(Announcement)
        )

        try:
            result = await self.session.execute(query)
        except IntegrityError as error:
            logger.info(error)
            raise DuplicateObject(error)
        return (result.scalar(), category)

    async def get_detail(
        self, announcement_id: ID
    ) -> tuple[Announcement, Category] | tuple[None, None]:
        query = select(Announcement).filter(Announcement.id == announcement_id)

        try:
            result = await self.session.execute(query)
        except DBAPIError as error:
            logger.info(error)
            raise InvalidInput(error)

        announcement: Announcement = result.scalar()

        if not announcement:
            return (None, None)

        category: Category = await self.get_or_create_category(
            id=announcement.category_id
        )
        return (announcement, category)

    async def get_list(
        self, limit: int = PAGINATE_LIMIT, offset: int = PAGINATE_OFFSET
    ) -> list[Announcement]:
        query = select(Announcement).offset(offset - 1).limit(limit)

        result = await self.session.execute(query)
        return result.scalars()

    async def delete(self, announcement_id: ID) -> None:
        query = delete(Announcement).filter(Announcement.id == announcement_id)

        try:
            await self.session.execute(query)
        except DBAPIError as error:
            logger.info(error)
            raise InvalidInput(error)

    async def get_or_create_category(self, name: str = None, id: ID = None) -> Category:
        query = select(Category).filter(
            Category.name == name if name else Category.id == id
        )
        result = await self.session.execute(query)
        category = result.scalar()
        if category:
            return category
        else:
            query = insert(Category).values(name=name).returning(Category)
            result = await self.session.execute(query)
            return result.scalar()
