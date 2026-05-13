from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.user import User
from schemas.user import UserCreate, UserUpdate
from services.common import CRUDService


class UserService(CRUDService[User, UserCreate, UserUpdate]):
    async def get_or_create_telegram_user(self, session: AsyncSession, telegram_id: int, username: str | None = None, full_name: str | None = None):
        stmt = select(User).where(User.telegram_id == telegram_id)
        result = await session.execute(stmt)
        user = result.scalar_one_or_none()
        if user:
            if username and user.username != username:
                user.username = username
            if full_name and user.full_name != full_name:
                user.full_name = full_name
            await session.commit()
            await session.refresh(user)
            return user
        user = User(telegram_id=telegram_id, username=username, full_name=full_name, referral_code=f'R{telegram_id}')
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user

    async def add_points(self, session: AsyncSession, user: User, points: int):
        user.points += points
        await session.commit()
        await session.refresh(user)
        return user


service = UserService(User)
