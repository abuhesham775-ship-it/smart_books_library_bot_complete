from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer(
        "/start - بدء الاستخدام\n"
        "/help - المساعدة\n"
        "/books - عرض الكتب\n"
        "/profile - الملف الشخصي\n"
        "/points - النقاط"
    )
