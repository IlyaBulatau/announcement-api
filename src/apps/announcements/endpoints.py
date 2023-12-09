from fastapi import APIRouter, Depends, Path
from fastapi.responses import JSONResponse
from fastapi_users.models import ID

from typing import Annotated

from src.database.models import User, Announcement
from src.apps.auth.routers import fastapi_users
from src.apps.announcements.manager import AnnouncementRepositoryManager
from src.apps.announcements.schemas import (
    AnnouncementCreate,
    AnnouncementRead,
    AnnouncementShortcut
)

router = APIRouter()
current_user = fastapi_users.current_user()
super_user = fastapi_users.current_user(superuser=True)

@router.post(
    "/",
    status_code=201,
    response_model=AnnouncementRead,
    response_description="Create and return new announcement",
)
async def create_announcement(
    announcement: AnnouncementCreate, 
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager),
    ):
    new_announcement, category = await manager.create(announcement, current_user.id)
    return AnnouncementRead(
        id=new_announcement.id,
        title=new_announcement.title,
        content=new_announcement.content,
        category=category.name,
        user_id=new_announcement.user_id,
        created_on=new_announcement.created_on
    )


@router.get(
        "/",
        response_model=list[AnnouncementShortcut],
        status_code=200,
        response_description="Return all announcement"
)
async def list_announcement(
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager), 
):
    announcements: list[Announcement] = await manager.get_list()
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
        response_description="Return certain announcement on ID"
)
async def detail_announcement(
    announcement_id: Annotated[ID, Path(description="announcement ID")],
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager), 
):
    announcement, category = await manager.get_detail(announcement_id)
    if announcement_id:
        return AnnouncementRead(
            id=announcement.id,
            title=announcement.title,
            content=announcement.content,
            category=category.name,
            user_id=announcement.user_id,
            created_on=announcement.created_on
        )
    else:
        return JSONResponse(
            content=f"announcement with {announcement_id} ID was not found",
            status_code=404,
            )


@router.delete(
        "/delete/{announcement_id}",
        status_code=200,
        response_description="Return all announcement"
)
async def delete_announcement(
    announcement_id: Annotated[ID, Path(description="announcement ID")],
    current_user: User = Depends(current_user),
    manager: AnnouncementRepositoryManager = Depends(AnnouncementRepositoryManager), 
):
    announcement, _ = await manager.get_detail(announcement_id)
    if current_user.id != announcement.user_id:
        return JSONResponse(
            content="You don't have permissions",
            status_code=403,
        )
    else:
        return JSONResponse(
            content="Successful",
            status_code=200,
        )