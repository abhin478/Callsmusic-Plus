# From Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
import asyncio
from config import BOT_OWNER

@Client.on_message(filters.command(["chatcast"]))
async def bye(client, message):
    sent=0
    failed=0
    if message.from_user.id in BOT_OWNER:
        lol = await message.reply("`Starting a Chatcast...`")
        if not message.reply_to_message:
            await lol.edit("Please Reply to a Message to Chatcast it 🥺!")
            return
        msg = message.reply_to_message.text
        async for dialog in client.iter_dialogs():
            try:
                await client.send_message(dialog.chat.id, msg)
                sent = sent+1
                await lol.edit(f"`ChatCasting...` /n/n**Sent to:** `{sent}` Chats /n**Failed in:** {failed} Chats")
            except:
                failed=failed+1
                await lol.edit(f"`ChatCasting...` /n/n**Sent to:** `{sent}` Chats /n**Failed in:** {failed} Chats")
            await asyncio.sleep(3)
        await message.reply_text(f"`ChatCasting Finished 😌` /n/n**Sent to:** `{sent}` Chats /n**Failed in:** {failed} Chats")