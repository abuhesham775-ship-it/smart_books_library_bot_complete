from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.book import Book
from db.models.recommendation import Recommendation
from schemas.recommendation import RecommendationCreate, RecommendationRead
from services.common import CRUDService


class RecommendationService(CRUDService[Recommendation, RecommendationCreate, RecommendationRead]):
    async def top_for_user(self, session: AsyncSession, user_id: int, limit: int = 10):
        stmt = select(Recommendation).where(Recommendation.user_id == user_id).order_by(Recommendation.score.desc()).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def similar_books(self, session: AsyncSession, book: Book, limit: int = 10):
        stmt = select(Book).where(Book.category_id == book.category_id, Book.id != book.id).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()


service = RecommendationService(Recommendation)
