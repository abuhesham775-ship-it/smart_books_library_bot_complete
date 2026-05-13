from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class AnalyticsEventBase(BaseModel):
    user_id: int | None = None
    event_name: str
    payload: str | None = None


class AnalyticsEventCreate(AnalyticsEventBase):
    pass


class AnalyticsEventRead(AnalyticsEventBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
