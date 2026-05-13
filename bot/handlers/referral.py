from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('referral'))
async def referral(message: Message):
    await message.answer('🔗 كود الإحالة سيظهر هنا.')
