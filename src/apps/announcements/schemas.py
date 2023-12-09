from pydantic import BaseModel

from fastapi_users.models import ID
from datetime import datetime

from src.database.models.category import EnumCategory


class AnnouncementCreate(BaseModel):
    title: str
    content: str
    category: EnumCategory

    class Config:
        orm_mode = True
        use_enum_values = True


class AnnouncementRead(AnnouncementCreate):
    id: ID
    user_id: ID
    category: str
    created_on: datetime


class AnnouncementShortcut(BaseModel):
    id: ID
    title: str
