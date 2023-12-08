from datetime import datetime

from sqlalchemy import orm
import sqlalchemy as db
from sqlalchemy.sql.functions import func


class BaseModel(orm.DeclarativeBase):
    __abstract__ = True
    
    created_on: orm.Mapped[datetime] = orm.mapped_column(
        db.DateTime(), server_default=func.now()
    )
    update_on: orm.Mapped[datetime] = orm.mapped_column(
        db.DateTime(), server_default=func.now(), onupdate=func.now()
    )
