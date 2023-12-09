from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from fastapi_users.models import ID

from typing import Annotated

from src.database.models import User, Comment
from src.apps.auth.routers import fastapi_users
from src.apps.categories.managers import CommentRepositoryManager


router = APIRouter()
super_user = fastapi_users.current_user(superuser=True)


@router.delete(
    "/comments/delete/{comment_id}",
    response_description="Return operation status",
    summary="Delete comment by ID"    
)
async def delete_comment(
    comment_id: Annotated[ID, Path(description="comment ID")],
    super_user: User = Depends(super_user),
    manager: CommentRepositoryManager = Depends(CommentRepositoryManager)
):
    """
    Accept:
    comment_id is ID comment that need delete
    super_user as validating the token and getting the user with uper user credentials
    manager object for make queries to database

    if comment_id is not found return 404 error
    if user doesn't have permission return 403 error
    """
    comment: Comment = await manager.get_detail(comment_id)
    if not comment:
        return JSONResponse(
            content={"Error": f"comment with {comment_id} ID was not found"},
            status_code=404,
        )
    else:
        await manager.delete(comment_id)
        return JSONResponse(
            content={"Status": "Successful"},
            status_code=200,
        )