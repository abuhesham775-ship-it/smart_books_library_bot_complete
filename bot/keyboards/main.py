from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🔎 بحث الكتب', callback_data='books:search')],
        [InlineKeyboardButton(text='👤 ملفي', callback_data='user:profile')],
        [InlineKeyboardButton(text='🏆 التحديات', callback_data='challenges:list')],
    ])
