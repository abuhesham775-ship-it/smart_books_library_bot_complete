from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def profile_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='🏅 الإنجازات', callback_data='user:achievements')],
        [InlineKeyboardButton(text='💳 الاشتراك', callback_data='user:subscriptions')],
    ])
