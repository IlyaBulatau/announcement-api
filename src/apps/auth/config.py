from fastapi_users.authentication import BearerTransport, JWTStrategy, AuthenticationBackend

from src.settings import JWT_SECRET


bearer_transport = BearerTransport(tokenUrl="auth/login")
JWT_TTL_SEC = 60 * 30

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET, lifetime_seconds=JWT_TTL_SEC)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)