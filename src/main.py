from fastapi import FastAPI, APIRouter

from src.endpoints import healthcheck_router
from src.apps.users import user_router
from src.apps.announcements import announcement_router
from src.apps.categories import categories_router

from src.apps.auth import auth_setup_router


API_ROOT_URL = "/api/v1"

DESCRIPTION = """
*Announcement API will helps your project. 🚀

## Users

* **Create users** 
* **Login users**
* **JWT auth**
* **Set up users permissions**

## Announcements

* **Create announcement by category**
* **Get list of announcement**
* **Get certain announcement by ID**
* **Delete certain announcement by ID**
* **Pagination**

## Comments

* **Delete category comment by ID**
"""

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
    main_router.include_router(
        categories_router, prefix="/categories", tags=["categories"]
    )
    auth_setup_router(main_router)

    app.include_router(main_router)


app = FastAPI(
    title="Announcement API service",
    version="0.0.1",
    contact={
        "name": "Developer",
        "url": "https://www.linkedin.com/in/ilya-bulatau-585133253",
        "email": "ilyabulatau@gmail.com",
    },
    openapi_url=API_ROOT_URL + "/openapi.json",
    description=DESCRIPTION,
    docs_url=API_ROOT_URL + "/docs",
    redoc_url=API_ROOT_URL + "/redoc",
)

setup_router(app)
