from sqlalchemy import select, insert
from fastapi_users.models import ID

from src.database.models import Announcement, Category
from src.database.manager import RepositoryManager
from src.apps.announcements.schemas import (
    AnnouncementCreate,
    AnnouncementRead,
    )


class AnnouncementRepositoryManager(RepositoryManager):

    async def create(self, announcement_schema: AnnouncementCreate, user_id: ID) -> tuple[Announcement, Category]:
        announcement = announcement_schema.model_dump()
        category: Category = await self.get_or_create_category(announcement.pop("category"))
        query = (
            insert(Announcement)
            .values(
                title=announcement.get("title"),
                content=announcement.get("content"), 
                category_id=category.id, 
                user_id=user_id
                )
            .returning(Announcement)
            )

        result = await self.session.execute(query)
        return (result.scalar(), category)

    async def get_detail(self, announcement_id: ID) -> tuple[Announcement, Category]:
        query = (
            select(Announcement)
            .filter(Announcement.id==announcement_id)
            )
        result = await self.session.execute(query)

        announcement: Announcement = result.scalar()
        category: Category = await self.get_or_create_category(id=announcement.category_id)
        return (announcement, category)
    
    async def get_list(self) -> list[Announcement]:
        query = select(Announcement)
        
        result = await self.session.execute(query)
        return result.scalars()

    
    async def delete(self) -> ...:
        ...

    async def get_or_create_category(self, name: str = None, id: ID = None) -> Category:
        query = select(Category).filter(Category.name==name if name else Category.id==id)
        result = await self.session.execute(query)
        category = result.scalar()
        if category:
            return category
        else:
            query = insert(Category).values(name=name).returning(Category)
            result = await self.session.execute(query)
            return result.scalar()   
        
