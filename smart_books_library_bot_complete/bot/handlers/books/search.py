from __future__ import annotations

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.utils.formatting import format_book
from bot.utils.text import books_empty

router = Router()


@router.message(Command('books'))
async def books_list(message: Message):
    await message.answer('استخدم /search ثم اسم الكتاب للبحث داخل المكتبة.')


@router.message(Command('search'))
async def search_books(message: Message):
    query = (message.text or '').replace('/search', '', 1).strip()
    if not query:
        await message.answer('اكتب بعد الأمر اسم الكتاب مثل: /search رواية')
        return
    await message.answer(f'🔎 جاري البحث عن: {query}')
