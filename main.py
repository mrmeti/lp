
from telethon.sync import TelegramClient, events
import os
api_id, api_hash = input('Enter your api_id: '), input('Enter your api_hash: ')
bot = TelegramClient('SecretBot', api_id, api_hash).start()

@bot.on(events.NewMessage(pattern=r'(وایسا|بصبر دان شه|دوز|بصب دان بشه)', func=lambda e: e.is_reply))
async def show_image(event):
    userid = await bot.get_me()
    if event.sender_id == userid.id:
        try:
            message = await event.get_reply_message()
            download = await bot.download_media(message)
            await bot.send_message('me', f'𝐁𝐨𝐭 𝐢𝐬 𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 𝐌𝐞𝐭𝐢𝐰𝐳 𝐓𝐞𝐚𝐦 💋🥂', file=download)
            os.remove(download)
        except Exception as e:
            await bot.send_message('me', f"خطایی دریافت شد:\n\n{e}")

bot.run_until_disconnected()

#Coded By MetiwzTeam 🤍