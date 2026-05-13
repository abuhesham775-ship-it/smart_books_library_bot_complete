from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routes import (
    admin, analytics, books, categories, challenges, notifications, points,
    recommendations, referral, reviews, social, subscriptions, users,
)
from core.config import settings
from core.logger import setup_logging
from db.models import Base
from db.session import engine

setup_logging()


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title=settings.app_name, version='1.0.0', lifespan=lifespan)

app.include_router(books.router, prefix='/api/books', tags=['books'])
app.include_router(users.router, prefix='/api/users', tags=['users'])
app.include_router(points.router, prefix='/api/points', tags=['points'])
app.include_router(recommendations.router, prefix='/api/recommendations', tags=['recommendations'])
app.include_router(categories.router, prefix='/api/categories', tags=['categories'])
app.include_router(reviews.router, prefix='/api/reviews', tags=['reviews'])
app.include_router(subscriptions.router, prefix='/api/subscriptions', tags=['subscriptions'])
app.include_router(admin.router, prefix='/api/admin', tags=['admin'])
app.include_router(referral.router, prefix='/api/referral', tags=['referral'])
app.include_router(analytics.router, prefix='/api/analytics', tags=['analytics'])
app.include_router(challenges.router, prefix='/api/challenges', tags=['challenges'])
app.include_router(notifications.router, prefix='/api/notifications', tags=['notifications'])
app.include_router(social.router, prefix='/api/social', tags=['social'])


@app.get('/')
async def root():
    return {'name': settings.app_name, 'status': 'ok'}


@app.get('/health')
async def health():
    return {'status': 'healthy'}
