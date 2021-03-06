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
                xxx_pratheek = f"šššš¼ š½ššš ššš¼ššš :\n\n**š£š„š¢šššš§ [ššØš”š](https://telegra.ph/file/ff13e3e82fb1ed734dfd5.jpg)**: ššššØ ššØ š”šš«š šØš©šš©šŖšØ š¤š šš”š” ššŖš£š š½š¤š©šØ. ššššØ šššØšØššš š ššš„šØ š¤š£ šŖš„ššš©šš£š šš£ šš«šš§š® šÆ š¢šš£šØ š¬šš©š š”šš«š šØš©šš©šŖšØ š¤š šš”š” šš¤š©šØ."
                for bot in BOT_LIST:
                    try:
                        yyy_pratheek = await app.send_message(bot, "/start")
                        aaa = yyy_pratheek.message_id
                        await asyncio.sleep(10)
                        zzz_pratheek = await app.get_history(bot, limit = 1)
                        for ccc in zzz_pratheek:
                            bbb = ccc.message_id
                        if aaa == bbb:
                            xxx_pratheek += f"š ššš šŖšš§š šš¢š©š ā¤ļø:\n\nš[{bot}](https://t.me/{bot}): šš  š¤"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"")
                                except Exception:
                                    pass
                            await app.read_history(bot)
                        else:
                            xxx_pratheek += f"\n\nš[{bot}](https://t.me/{bot}): š¢š” š„"
                            await app.read_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_pratheek += f"\n\nāļø šš®šš š°šµš²š°šøš²š± š¼š»:"
                xxx_pratheek += f"\n\n{last_update}\n({TIME_ZONE})"
                xxx_pratheek += f"\n\nšØš½š±š®šš²š š²šš²šæš šÆ šŗš¶š» </i>\nŠ¼Ī±āŃ Š²Ń|| š»šš½š°-š-ššššš“š¼ ||"
                xxx_pratheek += f"\n\nš¦šØšššš¦ššØššš¬ šš¢š”š”ššš§šš:-\nš¦šš”ššš£š¢š„š š¦šš„š©šš„\n&& š šØš ššš š¦šš„š©šš„"
                xxx_pratheek += f"\n\nš #TRYLUNA "
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_pratheek)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(180)
                        
app.run(main_pratheek())
