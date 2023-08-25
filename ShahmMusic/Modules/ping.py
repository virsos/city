import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ShahmMusic import BOT_NAME, StartTime, app
from ShahmMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping") | filters.command(["ب","البنك"],prefixes= ["/", "!","","#"]))
async def ping_Shahm(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} انتظر من فضلك..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""⌔︙ البنك : `{resp}ᴍs`

<b><u>{BOT_NAME} الحاله :</u></b>

⌔︙ **مدة التشغيل :** {uptime}
⌔︙ **الرام :** {mem}
⌔︙ **وحدة المعالجة المركزية :** {cpu}
⌔︙ **القرص :** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("الدعم", url=config.SUPPORT_CHAT),
                    InlineKeyboardButton(
                        "•CITY ›",
                        url="https://t.me/FPPPP6l",
                    ),
                ],
            ]
        ),
    )
