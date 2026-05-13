from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def challenges_menu() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='➕ انضم', callback_data='challenge:join:1')],
        [InlineKeyboardButton(text='✅ استلام', callback_data='challenge:claim:1')],
    ])
