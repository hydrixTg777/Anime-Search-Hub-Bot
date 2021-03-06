from bot import BOT_USERNAME, DOWNLOAD_DIR 
from pyrogram import Client, filters
from pyrogram.types import  CallbackQuery
from bot.helpers.tracemoe_api import tracemoe_trace

@Client.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hi Sir!",
        reply_to_message_id=update.message_id
    )

@Client.on_callback_query(filters.regex("close"))
async def close_menu(c: Client, cb: CallbackQuery):
    await c.delete_messages(
        chat_id=cb.message.chat.id,
        message_ids=cb.message.message_id
    )
    try:
        await c.delete_messages(
            chat_id=cb.message.chat.id,
            message_ids=cb.message.reply_to_message.message_id
        )
    except:
        pass
