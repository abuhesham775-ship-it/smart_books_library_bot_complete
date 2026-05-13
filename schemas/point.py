from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class PointTransactionBase(BaseModel):
    user_id: int
    points: int
    reason: str
    source: str | None = None


class PointTransactionCreate(PointTransactionBase):
    pass


class PointTransactionRead(PointTransactionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
