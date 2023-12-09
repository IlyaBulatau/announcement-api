from sqlalchemy import orm
import sqlalchemy as db
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.orm import validates
from sqlalchemy import orm

import uuid

from src.database.models.base import BaseModel


CONTENT_MIN_LENGTH = 256
TITLE_MAX_LENGTH = 256


class Announcement(BaseModel):
    __tablename__ = "announcements"
    __table_args__ = (
        CheckConstraint("char_length(content) > 255", name="content_string_min_length"),
    )

    id: orm.Mapped[db.UUID] = orm.mapped_column(
        db.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True
    )
    title: orm.Mapped[db.String] = orm.mapped_column(
        db.String(length=TITLE_MAX_LENGTH), nullable=False, unique=True
    )
    content: orm.Mapped[db.Text] = orm.mapped_column(
        db.Text(),
        nullable=False,
    )

    category_id: orm.Mapped[db.UUID] = orm.mapped_column(db.ForeignKey("categories.id"))
    user_id: orm.Mapped[db.UUID] = orm.mapped_column(db.ForeignKey("users.id"))

    @validates("content")
    def validate_content_length(self, key, content) -> str:
        if len(content) <= CONTENT_MIN_LENGTH:
            raise ValueError("content too short")
        return content
