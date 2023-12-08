from environs import Env
from pathlib import Path


BASE_DIR = Path(__name__).absolute().parent

ENV_FILE = ".env"
ENV = Env()
ENV.read_env(path=BASE_DIR / "env" / ENV_FILE)


class DatabaseSetting:
    POSTGRES_USER: str = ENV("POSTGRES_USER", "root")
    POSTGRES_PASSWORD: str = ENV("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = ENV("POSTGRES_DB", "name")
    POSTGRES_PORT: str | int = ENV("POSTGRES_PORT", "5432")
    POSTGRES_HOST: str = ENV("POSTGRES_HOST", "postgres")


    def get_url(self) -> str:
        url = \
        "postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}"
        
        return url.format(
            user=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            db=self.POSTGRES_DB,
        )
    
JWT_SECRET = ENV("JWT_SECRET")