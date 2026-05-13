from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class SubscriptionBase(BaseModel):
    user_id: int
    plan_name: str
    is_active: bool = True


class SubscriptionCreate(SubscriptionBase):
    pass


class SubscriptionUpdate(BaseModel):
    plan_name: str | None = None
    is_active: bool | None = None


class SubscriptionRead(SubscriptionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
