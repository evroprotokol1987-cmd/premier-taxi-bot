import os
import asyncio
from telethon import TelegramClient

BOT_TOKEN = os.getenv('BOT_TOKEN')
API_ID = 1234567  # O'zingizning api_id raqamingiz
API_HASH = 'sizning_api_hash'  # O'zingizning api_hash'ingiz

client = TelegramClient('my_session', API_ID, API_HASH)

async def main():
    print("Bot ulanmoqda...")
    await client.start(bot_token=BOT_TOKEN)
    print("Bot muvaffaqiyatli ishga tushdi va ishlayapti!")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
