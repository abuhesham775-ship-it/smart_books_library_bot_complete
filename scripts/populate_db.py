from __future__ import annotations

import asyncio

from db.session import AsyncSessionLocal, engine
from db.models import Base, Book, Category, User


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSessionLocal() as session:
        session.add_all([
            Category(name='General', description='Default category'),
            Book(title='Sample Book', author='Admin', description='Demo book'),
            User(telegram_id=123456789, username='admin', full_name='Admin User', points=100, referral_code='ADMIN123'),
        ])
        await session.commit()
    print('Database populated')


if __name__ == '__main__':
    asyncio.run(main())
