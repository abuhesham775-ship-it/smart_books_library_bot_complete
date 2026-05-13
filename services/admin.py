from __future__ import annotations

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from db.models.analytics import AnalyticsEvent
from db.models.book import Book
from db.models.challenge import Challenge
from db.models.point import PointTransaction
from db.models.review import Review
from db.models.user import User


class AdminService:
    async def stats(self, session: AsyncSession):
        users = await session.scalar(select(func.count()).select_from(User))
        books = await session.scalar(select(func.count()).select_from(Book))
        reviews = await session.scalar(select(func.count()).select_from(Review))
        points = await session.scalar(select(func.coalesce(func.sum(PointTransaction.points), 0)))
        challenges = await session.scalar(select(func.count()).select_from(Challenge))
        return {
            'users': int(users or 0),
            'books': int(books or 0),
            'reviews': int(reviews or 0),
            'points': int(points or 0),
            'challenges': int(challenges or 0),
        }

    async def recent_events(self, session: AsyncSession, limit: int = 20):
        stmt = select(AnalyticsEvent).order_by(AnalyticsEvent.id.desc()).limit(limit)
        result = await session.execute(stmt)
        return result.scalars().all()


service = AdminService()
