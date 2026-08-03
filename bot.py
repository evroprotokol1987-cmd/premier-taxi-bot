from telethon import TelegramClient, events
import asyncio
import time

# Созламалар
api_id = 33202290
api_hash = 'e90be200dbfa4e65cf584f4fd8c57a1d'
target_group = 'yuk_markazi_offical' 

client = TelegramClient('my_session', api_id, api_hash)

KEYWORDS = ['yuk', 'bor', 'ish', 'юқ', 'бор', 'иш']
last_sent_time = 0
PAUSE_DURATION = 30 

@client.on(events.NewMessage)
async def handler(event):
    global last_sent_time
    msg_text = event.raw_text
    if not msg_text:
        return

    # Калит сўзларни текшириш
    if any(word in msg_text.lower() for word in KEYWORDS):
        # Ўз-ўзингизга ва мақсадли гуруҳга юбормаслик учун
        if not event.out and getattr(event.chat, 'username', '') != target_group:
            current_time = time.time()
            if current_time - last_sent_time > PAUSE_DURATION:
                try:
                    final_text = (
                        f"{msg_text}\n\n"
                        "————————————————\n"
                        "🛣 Йўлларда эҳтиёт бўлинг! Сафарингиз бехатар бўлсин!\n"
                        "🤖 Ҳайдовчилар учун бот: @tezkor_avto_xizmat_bot"
                    )
                    await client.send_message(target_group, final_text)
                    last_sent_time = current_time
                    print(f"✅ Реклама юборилди: @{target_group}")
                except Exception as e:
                    print(f"❌ Хатолик: {e}")

async def main():
    await client.start()
    print("🚀 БОТ УЛАНДИ! Хабарларни кутяпман...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())