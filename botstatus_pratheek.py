from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_name = os.environ["SESSION_NAME"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_pratheek():
    async with app:
            while True:
                print("Checking...")
                GET_CHANNEL_OR_GROUP = await app.get_chat(int(CHANNEL_OR_GROUP_ID))
                CHANNEL_OR_GROUP_NAME = GET_CHANNEL_OR_GROUP.title
                CHANNEL_OR_GROUP_TYPE = GET_CHANNEL_OR_GROUP.type
                xxx_pratheek = f"𝙇𝙐𝙉𝘼 𝘽𝙊𝙏𝙎 𝙎𝙏𝘼𝙏𝙐𝙎 :\n\n**𝗣𝗥𝗢𝗝𝗘𝗖𝗧 𝗟𝗨𝗡𝗔**: 𝙏𝙝𝙞𝙨 𝙞𝙨 𝙡𝙞𝙫𝙚 𝙨𝙩𝙖𝙩𝙪𝙨 𝙤𝙛 𝙖𝙡𝙡 𝙇𝙪𝙣𝙖 𝘽𝙤𝙩𝙨. 𝙏𝙝𝙞𝙨 𝙈𝙚𝙨𝙨𝙖𝙜𝙚 𝙠𝙚𝙚𝙥𝙨 𝙤𝙣 𝙪𝙥𝙙𝙖𝙩𝙞𝙣𝙜 𝙞𝙣 𝙚𝙫𝙚𝙧𝙮 𝟯 𝙢𝙞𝙣𝙨 𝙬𝙞𝙩𝙝 𝙡𝙞𝙫𝙚 𝙨𝙩𝙖𝙩𝙪𝙨 𝙤𝙛 𝙖𝙡𝙡 𝙗𝙤𝙩𝙨."
                for bot in BOT_LIST:
                    try:
                        yyy_pratheek = await app.send_message(bot, "/start")
                        aaa = yyy_pratheek.message_id
                        await asyncio.sleep(10)
                        zzz_pratheek = await app.get_history(bot, limit = 1)
                        for ccc in zzz_pratheek:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xxx_pratheek += f"𝗠𝗔𝗗𝗘 𝗪𝗜𝗧𝗛 𝗟𝗢𝗩𝗘 ❤️:\n\n💕 **𝗟𝗨𝗡𝗔**: @{bot}\n💟 **𝗟𝗜𝗩𝗘**: I M AT REST  💤💤"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"💟 **SORRY GUYS SOME ISSUE !! @{bot} is AT SLEEP** 💤💤")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            xxx_pratheek += f"\n\n💕 **𝗟𝗨𝗡𝗔**: @{bot}\n💟 **𝗟𝗜𝗩𝗘**: alive 🔥"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_pratheek += f"\n\n✔️ 𝗟𝗮𝘀𝘁 𝗰𝗵𝗲𝗰𝗸𝗲𝗱 𝗼𝗻: {last_update} ({TIME_ZONE})\n\n<i>💘 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 𝗲𝘃𝗲𝗿𝘆 𝟯 𝗺𝗶𝗻 </i> - Made By||𝘼𝙇𝘼𝙉 𝙒𝘼𝙇𝙆𝙀𝙍 ||"
                xxx_pratheek += f"\n\n💟 #TRYLUNA "
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_pratheek)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(180)
                        
app.run(main_pratheek())
