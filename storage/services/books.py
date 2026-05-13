from __future__ import annotations

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from core.utils import normalize_query
from db.models.book import Book
from schemas.book import BookCreate, BookUpdate
from services.common import CRUDService


book_service = CRUDService[Book, BookCreate, BookUpdate](Book)


class BookService(CRUDService[Book, BookCreate, BookUpdate]):
    async def search(self, session: AsyncSession, query: str):
        q = f"%{normalize_query(query)}%"
        stmt = select(Book).where(func.lower(Book.title).like(q) | func.lower(Book.author).like(q))
        result = await session.execute(stmt)
        return result.scalars().all()

    async def list_by_category(self, session: AsyncSession, category_id: int):
        stmt = select(Book).where(Book.category_id == category_id)
        result = await session.execute(stmt)
        return result.scalars().all()

    async def increment_views(self, session: AsyncSession, book: Book):
        book.views_count += 1
        await session.commit()
        await session.refresh(book)
        return book

    async def increment_downloads(self, session: AsyncSession, book: Book):
        book.downloads_count += 1
        await session.commit()
        await session.refresh(book)
        return book


service = BookService(Book)
