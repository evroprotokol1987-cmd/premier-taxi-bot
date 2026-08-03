import os
import asyncio
from aiogram import Bot, Dispatcher, types

# Render'dagi Environment'dan tokeni avtomatik olamiz
BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def start_handler(message: types.Message):
    await message.answer("Assalomu alaykum! Bot muvaffaqiyatli ishlayapti.")

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
