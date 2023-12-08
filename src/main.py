from fastapi import FastAPI, APIRouter

from src import endpoints


API_ROOT_URL = "/api/v1"

main_router = APIRouter(prefix=API_ROOT_URL)

def setup_router(main_router: APIRouter = main_router) -> None:
    """
    It gets all router from endpoints module and include them to app
    """
    main_router.include_router(
        endpoints.healthcheck_router, prefix="/healthcheck", tags=["heatlcheck"]
        )
    
    app.include_router(main_router)

app = FastAPI(
    docs_url=API_ROOT_URL+"/docs",
    redoc_url=API_ROOT_URL+"/redoc")

setup_router()

