from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import orm, String

from src.database.models.base import BaseModel


class User(SQLAlchemyBaseUserTableUUID, BaseModel):
    __tablename__ = "users"

    username = orm.Mapped[str] = orm.mapped_column(
        String(length=32), unique=True, nullable=False
        )