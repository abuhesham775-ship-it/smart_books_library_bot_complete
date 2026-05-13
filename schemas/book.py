from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    title: str
    author: str
    description: str | None = None
    cover_url: str | None = None
    file_url: str | None = None
    category_id: int | None = None
    language: str | None = None
    published_year: int | None = None


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    description: str | None = None
    cover_url: str | None = None
    file_url: str | None = None
    category_id: int | None = None
    rating: float | None = None
    views_count: int | None = None
    downloads_count: int | None = None
    language: str | None = None
    published_year: int | None = None


class BookRead(BookBase):
    id: int
    rating: float = 0.0
    views_count: int = 0
    downloads_count: int = 0

    model_config = ConfigDict(from_attributes=True)
