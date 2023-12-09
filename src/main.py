from fastapi import FastAPI, APIRouter

from src.endpoints import healthcheck_router
from src.apps.users import user_router
from src.apps.announcements import announcement_router
from src.apps.auth import auth_setup_router


API_ROOT_URL = "/api/v1"

main_router = APIRouter(prefix=API_ROOT_URL)


def setup_router(app: FastAPI, main_router: APIRouter = main_router) -> None:
    """
    It gets all router and include them to app
    """
    main_router.include_router(
        healthcheck_router, prefix="/healthcheck", tags=["heatlchecks"]
    )
    main_router.include_router(user_router, prefix="/users", tags=["users"])
    main_router.include_router(
        announcement_router, prefix="/announcement", tags=["announcement"]
    )
    auth_setup_router(main_router)

    app.include_router(main_router)


app = FastAPI(
    docs_url=API_ROOT_URL + "/docs",
    redoc_url=API_ROOT_URL + "/redoc",
)

setup_router(app)
