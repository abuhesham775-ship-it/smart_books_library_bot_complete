from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.filters.admin import AdminFilter

router = Router()


@router.message(Command('admin'))
async def admin_panel(message: Message):
    if not await AdminFilter()(message):
        await message.answer('⛔ غير مصرح.')
        return
    await message.answer('لوحة الإدارة جاهزة.')
