from __future__ import annotations

from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards.main import main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "📚 أهلاً بك في Smart Books Library Bot\n"
        "ابحث عن الكتب، تابع النقاط، وشارك في التحديات.",
        reply_markup=main_menu(),
    )
