from aiogram import F, Router
from aiogram.types import CallbackQuery

router = Router()


@router.callback_query(F.data == 'user:subscriptions')
async def subscriptions(call: CallbackQuery):
    await call.answer('الاشتراكات ستكون متاحة هنا.', show_alert=True)
