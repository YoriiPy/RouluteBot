import aiosqlite
DB_NAME = "database.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""CREATE IF NOT EXISTS users (
                                    user_id TEXT,
                                    username TEXT, 
                                    
                                    roulette TEXT,
                                    roulette_message_id TEXT,
                                    roulette_chat_id TEXT
                                    
                        )""")
