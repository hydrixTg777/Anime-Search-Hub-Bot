from pyrogram import Client, filters
from bot import BOT_USERNAME
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["buttons", f"buttons@{BOT_USERNAME}"]))
async def addButtons(bot, update):
    try:
        links = update.text.split("\n")
    except:
        links = None
    msg = update.reply_to_message
    if msg and links:
        inline_keyboard = []
        inline_keyboard.append([InlineKeyboardButton(text="Direct Download",callback_data=links[1])])
        inline_keyboard.append([InlineKeyboardButton(text="TG File",callback_data=links[2])])
        await bot.copy_message(
            chat_id=update.chat.id,
            from_chat_id=msg.chat.id,
            message_id=msg.message_id,
            reply_markup=InlineKeyboardMarkup(inline_keyboard)
        )


