import sqlalchemy as db
from sqlalchemy import orm

import uuid

from src.database.models.base import BaseModel


CONTENT_MAX_LENGTH = 256


class Comment(BaseModel):
    __tablename__ = "comments"

    id: orm.Mapped[db.UUID] = orm.mapped_column(
        db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    content: orm.Mapped[db.String] = orm.mapped_column(
        db.String(length=CONTENT_MAX_LENGTH), nullable=False
    )
    category_id: orm.Mapped[db.UUID] = orm.mapped_column(db.ForeignKey("categories.id"))
    user_id: orm.Mapped[db.UUID] = orm.mapped_column(db.ForeignKey("users.id"))
