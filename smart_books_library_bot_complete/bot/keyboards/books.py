from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def book_actions(book_id: int) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='📄 التفاصيل', callback_data=f'book:details:{book_id}')],
        [InlineKeyboardButton(text='⬇️ إرسال الملف', callback_data=f'book:send:{book_id}')],
    ])
