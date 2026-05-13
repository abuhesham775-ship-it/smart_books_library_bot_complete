from __future__ import annotations

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from db.session import get_db
from services.users import service as user_service


async def get_current_user_id(x_user_id: int | None = Header(default=None, alias='X-User-Id')) -> int:
    if x_user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='X-User-Id header is required for demo auth')
    return x_user_id


async def get_current_user(session: AsyncSession = Depends(get_db), user_id: int = Depends(get_current_user_id)):
    user = await user_service.get(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


def is_admin(user_id: int) -> bool:
    return user_id in settings.admin_id_list
