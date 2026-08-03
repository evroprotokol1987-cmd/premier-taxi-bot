import os
import asyncio
from telethon import TelegramClient

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = 1234567  # O'zingizning api_id raqamingiz
API_HASH = 'sizning_api_hash'  # O'zingizning api_hash'ingiz

async def main():
    # Client'ni to'g'ridan-to'g'ri async funksiya ichida yaratamiz
    client = TelegramClient('my_session', API_ID, API_HASH)
    
    print("Bot ulanmoqda...")
    await client.start(bot_token=BOT_TOKEN)
    print("Bot muvaffaqiyatli ishga tushdi va ishlayapti!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
