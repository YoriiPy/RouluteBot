from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def admin_start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🎲 Создать конкурс", callback_data="create_contest")
    return keyboard.as_markup()

def back_to_start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="⬅️ Назад", callback_data="back_to_start")
    return keyboard.as_markup()

def accept_contest_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Да ✅")
    keyboard.button(text="❌ Нет", callback_data="accept_contest")
    back_start = InlineKeyboardBuilder.from_markup(back_to_start_keyboard())
    keyboard.attach(back_start)
    keyboard.adjust(2, 1)
    return keyboard.as_markup()
