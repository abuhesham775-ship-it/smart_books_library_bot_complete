from __future__ import annotations

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message

from core.config import settings


class ForceJoinMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        if isinstance(event, Message) and settings.force_join_chat_id:
            member = data.get('chat_member')
            if member is None:
                return await handler(event, data)
        return await handler(event, data)
