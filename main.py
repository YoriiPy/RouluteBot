from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from database import models
from handlers.admin_handlers import router as admin_router



import os
import asyncio



file = load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    # 1. Сначала запускаем базу данных и обновляем ссылки в клавиатурах

    # 2. Инициализируем бота
    await models.init_db()
    bot = Bot(token=BOT_TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_router(admin_router)
    # 3. Запускаем бесконечный опрос серверов Telegram
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())