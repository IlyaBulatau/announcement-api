from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.settings import DatabaseSetting


async_engine = create_async_engine(
    url=DatabaseSetting().get_url(),
    future=True,
)

async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


async def get_async_session(commit: bool = True) -> AsyncSession:
    session = async_session()
    try:
        yield session
        if commit:
            await session.commit()
    except Exception as e:
        await session.rollback()
    finally:
        await session.close()
