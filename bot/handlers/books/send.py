from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data.startswith('book:send:'))
async def book_send(call: CallbackQuery):
    await call.answer('إرسال الملف جاهز لاحقًا من خلال storage/files.py', show_alert=True)
