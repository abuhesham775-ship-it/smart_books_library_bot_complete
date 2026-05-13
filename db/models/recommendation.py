from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base, TimestampMixin


class Recommendation(Base, TimestampMixin):
    __tablename__ = 'recommendations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id', ondelete='CASCADE'), nullable=False, index=True)
    score: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    reason: Mapped[str | None] = mapped_column(String(255), nullable=True)

    user = relationship('User')
    book = relationship('Book', back_populates='recommendations')
