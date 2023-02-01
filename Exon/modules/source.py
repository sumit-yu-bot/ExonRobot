from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Exon import app as pbot

ABISHNOIX = "https://te.legra.ph/file/a2302bee25471caf1020e.jpg"


@pbot.on_message(filters.command(["repo", "source"]))
async def repo(_, message):
    await message.reply_photo(
        photo=ABISHNOIX,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**

**ʀᴇᴘᴏ ᴏᴡɴᴇʀ  : [ꜱᴜᴍɪᴛ ](https://t.me/ll_sumit_ll)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
**ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ :** `2.69`
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴍᴜꜱɪᴄ•", url="https://te.legra.ph/file/be1d79f0f8d48c7e65c43.mp4"
                    ),
                    InlineKeyboardButton(
                        "•ʀᴏʙᴏᴛ•", url="https://te.legra.ph/file/be1d79f0f8d48c7e65c43.mp4"
                    ),
                ]
            ]
        ),
    )
