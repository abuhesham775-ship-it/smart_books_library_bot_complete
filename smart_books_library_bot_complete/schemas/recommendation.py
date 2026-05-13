from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class RecommendationBase(BaseModel):
    user_id: int
    book_id: int
    score: float = 0.0
    reason: str | None = None


class RecommendationCreate(RecommendationBase):
    pass


class RecommendationRead(RecommendationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
