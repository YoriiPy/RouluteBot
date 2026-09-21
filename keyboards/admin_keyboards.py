from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import requests as rq

def admin_start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="🎲 Создать конкурс", callback_data="create_contest")
    keyboard.button(text="👤 Мои конкурсы", callback_data="my_contest")
    return keyboard.as_markup()

def back_to_start_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="⬅️ Назад", callback_data="back_to_start")
    return keyboard.as_markup()

def accept_contest_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Да ✅", callback_data="no_accept_contest")
    keyboard.button(text="❌ Нет", callback_data="accept_contest")
    back_start = InlineKeyboardBuilder.from_markup(back_to_start_keyboard())
    keyboard.attach(back_start)
    keyboard.adjust(2, 1)
    return keyboard.as_markup()

async def get_contest_keyboard(user_id: str):
    keyboard = InlineKeyboardBuilder()
    result = await rq.get_roulette_keyboard(user_id)

    for roulette in result:
        keyboard.button(text=result.splitlines()[0].replace("Приз: ", "").strip(), callback_data=roulette)
    return keyboard.as_markup()

