from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base, TimestampMixin


class Review(Base, TimestampMixin):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'), nullable=False, index=True)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    comment: Mapped[str | None] = mapped_column(Text, nullable=True)

    user = relationship('User', back_populates='reviews')
    book = relationship('Book', back_populates='reviews')
