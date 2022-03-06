from bot import BOT_USERNAME
from pyrogram import Client, filters
from helpers.kitsu_api import kitsu_get_title, kitsu_get_anime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["kitsu", f"kitsu@{BOT_USERNAME}"]))
async def search_anime_kitsu(bot, update):
    try:
        if update.reply_to_message:
            name = update.reply_to_message.text
        else:
            name = update.text.split(" ", maxsplit=1)[1]
    except:
        name = None
    if name:
        await bot.send_message(
                chat_id=update.chat.id,
                text=f"<b>Searching for:</b> {name}",
                reply_to_message_id=update.message_id
            )
        titles, aids = await kitsu_get_title(name)
        if titles:
            inline_keyboard = []
            for aid in aids:
                inline_keyboard.append([InlineKeyboardButton(text=titles[aids.index(aid)], callback_data=f"kitsuanime_{aid}")])
            inline_keyboard.append([InlineKeyboardButton(text="Close",callback_data="close")])
            await bot.send_message(
                chat_id=update.chat.id,
                text="<b>Search Results:</b>",
                reply_markup=InlineKeyboardMarkup(inline_keyboard),
                reply_to_message_id=update.message_id
            )




