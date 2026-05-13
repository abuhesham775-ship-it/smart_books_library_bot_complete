from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from bot.keyboards.profile import profile_menu

router = Router()


@router.message(Command('profile'))
async def profile(message: Message):
    await message.answer('👤 ملفك الشخصي', reply_markup=profile_menu())


@router.callback_query(F.data == 'user:profile')
async def profile_callback(call: CallbackQuery):
    await call.message.answer('👤 ملفك الشخصي', reply_markup=profile_menu())
    await call.answer()
