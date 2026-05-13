from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('notifications'))
async def notifications(message: Message):
    await message.answer('🔔 لا توجد إشعارات حالياً.')
