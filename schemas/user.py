from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    telegram_id: int | None = None
    username: str | None = None
    full_name: str | None = None
    bio: str | None = None
    is_premium: bool = False
    is_active: bool = True
    referral_code: str | None = None


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    telegram_id: int | None = None
    username: str | None = None
    full_name: str | None = None
    bio: str | None = None
    points: int | None = None
    is_premium: bool | None = None
    is_active: bool | None = None
    referral_code: str | None = None


class UserRead(UserBase):
    id: int
    points: int = 0

    model_config = ConfigDict(from_attributes=True)
