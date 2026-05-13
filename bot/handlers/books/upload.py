from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('upload_book'))
async def upload_book(message: Message):
    await message.answer('رفع الكتب متاح من لوحة الإدارة أو API حالياً.')
