from fastapi_users import FastAPIUsers
from fastapi import APIRouter

import uuid

from src.apps.auth.config import auth_backend
from src.apps.auth.manager import get_user_manager
from src.database.models.user import User
from src.apps.auth.schemas import UserCreate, UserRead


fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)

def auth_setup_router(main_router: APIRouter):
    tags = ["auth"]
    prefix = "/auth"

     # https://fastapi-users.github.io/fastapi-users/12.1/usage/flow/#request_1
    main_router.include_router(
        fastapi_users.get_auth_router(auth_backend),
        prefix=prefix,
        tags=tags,
        )
    main_router.include_router(
        fastapi_users.get_register_router(UserRead, UserCreate),
        prefix=prefix,
        tags=tags,
        )
    