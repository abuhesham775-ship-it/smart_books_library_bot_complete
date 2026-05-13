from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class NotificationBase(BaseModel):
    user_id: int | None = None
    title: str
    message: str
    is_read: bool = False
    type: str | None = None


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(BaseModel):
    title: str | None = None
    message: str | None = None
    is_read: bool | None = None
    type: str | None = None


class NotificationRead(NotificationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
