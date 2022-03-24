from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random



ALL_PIC = [
 "https://telegra.ph/file/4f17724d822a443817750.jpg",
 "https://telegra.ph/file/7ecc4cc9c6128b689fdbd.jpg",
 "https://telegra.ph/file/1681e7fbc2267c618273d.jpg",
 "https://telegra.ph/file/aa28fa6ccac3e4dead164.jpg"
]









START_MESSAGE= """ Hey {} This bot's work on progress⚙️
"""



@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    await msg.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=START_MESSAGE.format(msg.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇᴢ ᴄʜᴀɴɴᴇʟ", url="https://t.me/ZPB_CODES")
           ]]
           )
    )
