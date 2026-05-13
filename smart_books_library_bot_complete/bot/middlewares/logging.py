from __future__ import annotations

import logging

from aiogram.dispatcher.middlewares.base import BaseMiddleware


class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        logging.getLogger('bot').info('Update received: %s', type(event).__name__)
        return await handler(event, data)
