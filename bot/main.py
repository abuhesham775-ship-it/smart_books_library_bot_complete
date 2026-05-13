from __future__ import annotations

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from bot.handlers import router as handlers_router
from bot.middlewares.auth import AuthMiddleware
from bot.middlewares.force_join import ForceJoinMiddleware
from bot.middlewares.logging import LoggingMiddleware
from bot.middlewares.rate_limit import RateLimitMiddleware
from core.config import settings
from core.logger import setup_logging


async def main() -> None:
    setup_logging()
    if not settings.bot_token:
        raise RuntimeError('BOT_TOKEN is required')

    bot = Bot(token=settings.bot_token)
    storage = MemoryStorage()

    if settings.bot_use_redis:
        redis = Redis.from_url(settings.redis_url)
        storage = RedisStorage(redis=redis)

    dp = Dispatcher(storage=storage)
    dp.include_router(handlers_router)

    dp.message.middleware(LoggingMiddleware())
    dp.message.middleware(RateLimitMiddleware())
    dp.message.middleware(ForceJoinMiddleware())
    dp.message.middleware(AuthMiddleware())

    logging.info('Bot started')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
