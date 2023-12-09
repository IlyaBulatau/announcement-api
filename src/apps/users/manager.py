from sqlalchemy import update

from src.database.models import User
from src.apps.users.schemas import UserUpdate
from src.database.manager import RepositoryManager


class UserRepositoryManager(RepositoryManager):
    async def set_permission(self, user_schema: UserUpdate) -> User | None:
        query = (
            update(User)
            .filter(User.username == user_schema.username)
            .values(is_superuser=True)
            .returning(User)
        )

        result = await self.session.execute(query)
        return result.scalar()
