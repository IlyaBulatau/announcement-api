from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.apps.auth.routers import fastapi_users
from src.database.models.user import User
from src.apps.auth.schemas import UserRead
from src.apps.users.manager import UserRepositoryManager
from src.apps.users.schemas import UserUpdate

router = APIRouter()
super_user = fastapi_users.current_user(superuser=True)


@router.patch(
    "/set_permission",
    response_model=UserRead,
    status_code=200,
    response_description="Return user fields that was changed",
    summary="Mod user object"
)
async def protected_route(
    user_update_schema: UserUpdate,
    user: User = Depends(super_user),
    manager: UserRepositoryManager = Depends(UserRepositoryManager),
):
    """
    Accept:
    user_update_schema with field for update
    user as validator super user
    manager for work with query to database

    if user is not found return 404 error
    """
    user = await manager.set_permission(user_update_schema)
    if user:
        return UserRead(**user.__dict__)
    return JSONResponse(
        content={"Status": "User is not found"},
        status_code=200
        )
