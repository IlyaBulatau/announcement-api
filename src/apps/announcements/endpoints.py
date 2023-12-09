from fastapi import APIRouter, Depends, Path, Query
from fastapi.responses import JSONResponse
from fastapi_users.models import ID

from typing import Annotated

from src.apps.announcements.constances import PAGINATE_LIMIT, PAGINATE_OFFSET
from src.database.models import User, Announcement
from src.apps.auth.routers import fastapi_users
from src.apps.announcements.manager import AnnouncementRepositoryManager
from src.apps.announcements.schemas import (
    AnnouncementCreate,
    AnnouncementRead,
    AnnouncementShortcut,
)

router = APIRouter()
current_user = fastapi_users.current_user()


@router.post(
    "/",
    status_code=201,
    response_model=AnnouncementRead,
    response_description="Return data with new announcement object",
    summary="Create new announcement",
)
async def create_announcement(
    announcement: AnnouncementCreate,
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager),
):
    """
    Accept:
    announcement schema,
    current_user as validating the token and getting the current user
    manager object for make queries to database

    Create new announcement in database and return schema
    also create category if it is not exists(and valide)
    """
    new_announcement, category = await manager.create(announcement, current_user.id)
    return AnnouncementRead(
        id=new_announcement.id,
        title=new_announcement.title,
        content=new_announcement.content,
        category=category.name,
        user_id=new_announcement.user_id,
        created_on=new_announcement.created_on,
    )


@router.get(
    "/",
    response_model=list[AnnouncementShortcut],
    status_code=200,
    response_description="Return list of announcement objects on paginate",
    summary="Get all announcement",
)
async def list_announcement(
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager),
    limit: Annotated[
        int, Query(ge=1, le=100, description="number of results to be returned")
    ] = PAGINATE_LIMIT,
    offset: Annotated[
        int, Query(ge=1, le=100000, description="starting from number")
    ] = PAGINATE_OFFSET,
):
    """
    Accept:
    current_user as validating the token and getting the current user
    manager object for make queries to database

    Return list of Announcement from database
    """

    announcements: list[Announcement] = await manager.get_list(limit, offset)
    return [
        AnnouncementShortcut(
            id=announcement.id,
            title=announcement.title,
        )
        for announcement in announcements
    ]


@router.get(
    "/{announcement_id}",
    response_model=AnnouncementRead,
    status_code=200,
    response_description="Return certain announcement",
    summary="Get announcement by ID",
)
async def detail_announcement(
    announcement_id: Annotated[ID, Path(description="announcement ID")],
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager),
):
    """
    Accept:
    announcement_id for search it in database
    current_user as validating the token and getting the current user
    manager object for make queries to database

    Return certain announcement on ID
    if announcement_id is not found return 404 error
    """

    announcement, category = await manager.get_detail(announcement_id)
    if announcement:
        return AnnouncementRead(
            id=announcement.id,
            title=announcement.title,
            content=announcement.content,
            category=category.name,
            user_id=announcement.user_id,
            created_on=announcement.created_on,
        )
    else:
        return JSONResponse(
            content={"Error": f"announcement with {announcement_id} ID was not found"},
            status_code=404,
        )


@router.delete(
    "/delete/{announcement_id}",
    status_code=200,
    response_description="Return dict with operation status",
    summary="Delete announcement by ID",
)
async def delete_announcement(
    announcement_id: Annotated[ID, Path(description="announcement ID")],
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager),
):
    """
    Accept:
    announcement_id for search it in database
    current_user as validating the token and getting the current user
    manager object for make queries to database

    if announcement_id is not found return 404 error
    if the announcement does not belong to the current user
    return 403 error
    """

    announcement, _ = await manager.get_detail(announcement_id)
    if not announcement:
        return JSONResponse(
            content={"Error": f"announcement with {announcement_id} ID was not found"},
            status_code=404,
        )
    if current_user.id != announcement.user_id:
        return JSONResponse(
            content={"Error": "You don't have permissions"},
            status_code=403,
        )
    else:
        await manager.delete(announcement_id)
        return JSONResponse(
            content={"Status": "Successful"},
            status_code=200,
        )
