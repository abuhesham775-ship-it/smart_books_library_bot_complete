from aiogram import F, Router
from aiogram.types import Message

router = Router()


@router.message(F.text)
async def fallback(message: Message):
    await message.answer('اكتب /help لمعرفة الأوامر المتاحة.')
