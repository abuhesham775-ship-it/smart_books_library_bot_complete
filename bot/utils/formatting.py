from __future__ import annotations

from db.models.book import Book
from db.models.user import User


def format_book(book: Book) -> str:
    return (
        f"📘 {book.title}\n"
        f"✍️ {book.author}\n"
        f"⭐ {book.rating:.1f} | 👁 {book.views_count} | ⬇️ {book.downloads_count}\n"
        f"{book.description or ''}"
    )


def format_user(user: User) -> str:
    return (
        f"👤 {user.full_name or 'مستخدم'}\n"
        f"@{user.username or '—'}\n"
        f"🏆 النقاط: {user.points}"
    )
