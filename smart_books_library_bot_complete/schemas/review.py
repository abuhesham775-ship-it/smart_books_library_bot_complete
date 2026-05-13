from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ReviewBase(BaseModel):
    user_id: int
    book_id: int
    rating: float
    comment: str | None = None


class ReviewCreate(ReviewBase):
    pass


class ReviewUpdate(BaseModel):
    rating: float | None = None
    comment: str | None = None


class ReviewRead(ReviewBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
