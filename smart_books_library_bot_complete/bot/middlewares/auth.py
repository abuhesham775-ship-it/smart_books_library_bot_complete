from __future__ import annotations

from aiogram.dispatcher.middlewares.base import BaseMiddleware


class AuthMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        return await handler(event, data)
