from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith('book:details:'))
async def book_details(call: CallbackQuery):
    await call.answer('تفاصيل الكتاب غير مربوطة بقاعدة البيانات بعد.', show_alert=True)
