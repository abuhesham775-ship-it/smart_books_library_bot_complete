from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith('challenge:join:'))
async def join(call: CallbackQuery):
    await call.answer('تم تسجيل طلب الانضمام للتحدي.', show_alert=True)
