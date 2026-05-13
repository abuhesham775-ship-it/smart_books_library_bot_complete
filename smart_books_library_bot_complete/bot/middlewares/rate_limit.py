from __future__ import annotations

import time
from collections import defaultdict, deque

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message


class RateLimitMiddleware(BaseMiddleware):
    def __init__(self, limit: int = 5, interval: int = 3):
        self.limit = limit
        self.interval = interval
        self.events = defaultdict(lambda: deque(maxlen=limit * 2))

    async def __call__(self, handler, event, data):
        user_id = getattr(getattr(event, 'from_user', None), 'id', None)
        if user_id is None:
            return await handler(event, data)
        now = time.monotonic()
        dq = self.events[user_id]
        while dq and now - dq[0] > self.interval:
            dq.popleft()
        if len(dq) >= self.limit:
            if isinstance(event, Message):
                await event.answer('⏳ أرسل الرسائل ببطء أكثر من فضلك.')
            return None
        dq.append(now)
        return await handler(event, data)
