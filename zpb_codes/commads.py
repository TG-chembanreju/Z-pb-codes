from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random



ALL_PIC = [
 "https://telegra.ph/file/21eae28fe6ee6776ef0b9.jpg",
 "https://telegra.ph/file/c273ae2226885e757a886.jpg"









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
