from __future__ import annotations

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base, TimestampMixin


class SocialPost(Base, TimestampMixin):
    __tablename__ = 'social_posts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    book_id: Mapped[int | None] = mapped_column(ForeignKey('books.id', ondelete='SET NULL'), nullable=True)
    likes_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    user = relationship('User', back_populates='social_posts')
    comments = relationship('SocialComment', back_populates='post', cascade='all, delete-orphan')


class SocialComment(Base, TimestampMixin):
    __tablename__ = 'social_comments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey('social_posts.id', ondelete='CASCADE'), nullable=False, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    is_hidden: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    post = relationship('SocialPost', back_populates='comments')
