from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class SocialPostBase(BaseModel):
    user_id: int
    content: str
    book_id: int | None = None
    likes_count: int = 0


class SocialPostCreate(SocialPostBase):
    pass


class SocialPostRead(SocialPostBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class SocialCommentBase(BaseModel):
    post_id: int
    user_id: int
    content: str
    is_hidden: bool = False


class SocialCommentCreate(SocialCommentBase):
    pass


class SocialCommentRead(SocialCommentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
