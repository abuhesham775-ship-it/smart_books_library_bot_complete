from __future__ import annotations

from sqlalchemy import ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.models.base import Base, TimestampMixin


class Book(Base, TimestampMixin):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    author: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    cover_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    file_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    category_id: Mapped[int | None] = mapped_column(ForeignKey('categories.id', ondelete='SET NULL'), nullable=True)
    rating: Mapped[float] = mapped_column(Float, default=0.0, nullable=False)
    views_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    downloads_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    language: Mapped[str | None] = mapped_column(String(50), nullable=True)
    published_year: Mapped[int | None] = mapped_column(Integer, nullable=True)

    category = relationship('Category', back_populates='books')
    reviews = relationship('Review', back_populates='book', cascade='all, delete-orphan')
    recommendations = relationship('Recommendation', back_populates='book', cascade='all, delete-orphan')
