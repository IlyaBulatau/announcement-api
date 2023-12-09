from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from src.apps.auth.routers import fastapi_users
from src.database.models.user import User
from src.apps.auth.schemas import UserUpdate, UserRead
from src.apps.users.manager import UserRepositoryManager


router = APIRouter()
super_user = fastapi_users.current_user(superuser=True)

@router.post(
        "/set_permission",
        response_model=UserRead,
        status_code=200,
        response_description="The response containe user fields that was changed"
        )
async def protected_route(
    user_update_schema: UserUpdate,
    user: User = Depends(super_user), 
    manager: UserRepositoryManager = Depends(UserRepositoryManager)
    ):
    user = await manager.set_permission(user_update_schema)
    if user:
        return UserRead(**user.__dict__) 
    return JSONResponse(content="User is not found")
    