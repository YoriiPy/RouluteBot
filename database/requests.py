import aiosqlite
from aiosqlite import cursor

DB_NAME = "database.db"

async def add_roulette(user_id : str, username: str, roulette : str, roulette_message_id : str, roulette_chat_id : str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO roulette VALUES (?, ?, ?, ?, ?)", (user_id, username, roulette, roulette_message_id, roulette_chat_id))
        await db.commit()

async def get_roulette(user_id : str):
    async with aiosqlite.connect(DB_NAME) as db:
        try:
            async with db.execute("SELECT roulette, roulette_message_id, roulette_chat_id FROM roulette FROM users WHERE user_id = ?", (user_id,)) as cursor:
                if await cursor.fetchone() is not None:
                    res = await cursor.fetchone()
                    return cursor.fetchone()
                else:
                    return None

        except Exception:
            pass

async def get_roulette_keyboard(user_id : str):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT roulette FROM users WHERE user_id = ?", (user_id, )) as cursor:
            if await cursor.fetchall() is not None:
                res = await cursor.fetchall()
                lists = []

                for text in res:
                    lists.append(text[0])

                return lists
            else:
                return []


