import os
import asyncio
from aiohttp import web
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "8858194914:AAEFVpxVzC9oR6dTy2qEPn6C723RP1Tt3P4"
PORT = int(os.getenv('PORT', 10000))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="📞 Admin bilan bog'lanish", url="https://t.me/premier_pro_taxi")
    builder.button(text="🤖 Yandex rasmiy boti", url="https://t.me/yandex_rasmiy_bot")
    builder.button(text="📞 Telefon qilish (+998 33 559-20-20)", url="tel:+998335592020")
    builder.button(text="📍 Ofis manzili va mo'ljal", callback_data="office_location")
    builder.button(text="🤲 Safar duosi", callback_data="travel_dua")
    builder.button(text="💵 Dollar kursi (NBU)", url="https://nbu.uz/jismoniy-shaxslar-valyutalar-kursi")
    builder.button(text="⚖️ Ma'muriy jarimalar", url="https://www.ejarima.uz/oz/search-admin")
    builder.button(text="🚸 Yo'l belgilari", url="https://uzavtoyolbelgi.uz/uz/dorojnie/znaki")
    builder.adjust(1)

    welcome_text = (
        "Assalomu alaykum! Yandex Go rasmiy hamkori "
        "**PREMIER PRO TAXI** rasmiy botiga xush kelibsiz.\n\n"
        "Taxoparkga a'zo bo'lish, haydovchilar uchun takliflar va qulayliklar "
        "uchun adminlar bilan bog'laning, telefon raqam, telegram profil "
        "yoki ofisimizga kelib barcha ma'lumotni olib ulanib oling.\n\n"
        "🏢 **Manzil:** Jizzax shahar, Islom Karimov ko‘chasi, 7-uy\n"
        "🎯 **Mo‘ljal:** O'rda sanatoriyasi"
    )
    
    await message.answer(welcome_text, parse_mode="Markdown", reply_markup=builder.as_markup())

@dp.callback_query(lambda c: c.data == "office_location")
async def office_callback(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📍 **Bizning manzilimiz:**\n"
        "Jizzax shahar, Islom Karimov ko‘chasi, 7-uy\n"
        "Mo‘ljal: O'rda sanatoriyasi\n\n"
        "Sizni ofisimizda kutib qolamiz!"
    , parse_mode="Markdown")

@dp.callback_query(lambda c: c.data == "travel_dua")
async def dua_callback(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🤲 **Safar duosi:**\n\n"
        "«Субҳаналлазий саххора лана ҳаза ва ма кунна лаҳу муқринийн. Ва инна ила Роббина ламунқолибун».\n\n"
        "🧳 Safaringiz bezavol va barokatli bo'lsin!"
    , parse_mode="Markdown")

async def handle(request):
    return web.Response(text="Bot is running!")

async def web_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()

async def main():
    await web_server()
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
