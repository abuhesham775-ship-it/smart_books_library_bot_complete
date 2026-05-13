from aiogram.filters import Filter
from aiogram.types import Message

from core.config import settings


class AdminFilter(Filter):
    async def __call__(self, message: Message) -> bool:
        return bool(message.from_user and message.from_user.id in settings.admin_id_list)
