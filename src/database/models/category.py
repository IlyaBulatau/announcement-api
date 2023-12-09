import sqlalchemy as db
from sqlalchemy import orm

import uuid
from enum import Enum

from src.database.models.base import BaseModel


class EnumCategory(str, Enum):
    sale:     str = "sale"
    purchase: str = "purchase"
    services: str = "services"


class Category(BaseModel):
    __tablename__ = "categories"

    id: orm.Mapped[db.UUID] = orm.mapped_column(
        db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
        )
    name: orm.Mapped[db.Enum] = orm.mapped_column(
        db.Enum(EnumCategory), nullable=False, unique=True
    )