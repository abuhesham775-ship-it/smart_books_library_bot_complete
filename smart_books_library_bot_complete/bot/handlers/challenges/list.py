from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards.challenges import challenges_menu

router = Router()


@router.message(Command('challenges'))
async def challenges_list(message: Message):
    await message.answer('🏁 التحديات', reply_markup=challenges_menu())
