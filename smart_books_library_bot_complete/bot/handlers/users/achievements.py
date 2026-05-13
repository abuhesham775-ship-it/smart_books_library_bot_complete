from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == 'user:achievements')
async def achievements(call: CallbackQuery):
    await call.answer('لا توجد إنجازات بعد.', show_alert=True)
