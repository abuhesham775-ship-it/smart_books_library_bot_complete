from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith('challenge:claim:'))
async def claim(call: CallbackQuery):
    await call.answer('تم تجهيز استلام المكافأة.', show_alert=True)
