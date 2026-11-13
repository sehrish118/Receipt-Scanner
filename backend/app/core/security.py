import uuid
from datetime import datetime, timedelta, timezone

import jwt
from pwdlib import PasswordHash

from app.core.config import get_settings

settings = get_settings()

password_hash = PasswordHash.recommended()
ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    return password_hash.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return password_hash.verify(plain, hashed)


def create_access_token(user_id: uuid.UUID) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.access_token_expire_minutes
    )
    payload = {"sub": str(user_id), "exp": expire}
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def decode_access_token(token: str) -> uuid.UUID | None:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        return uuid.UUID(payload["sub"])
    except (jwt.PyJWTError, KeyError, ValueError):
        return None
