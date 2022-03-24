from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery

START_MESSAGE= """ Hey {} This bot's work on progress⚙️
"""



@Client.on_message(filters.command("start"))
async def start_msg(bot, msg):
    await msg.reply_text(
        text=START_MESSAGE.format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("ᴜᴩᴅᴀᴛᴇᴢ ᴄʜᴀɴɴᴇʟ", url="https://t.me/ZPB_CODES")
           ]]
           )
    )
