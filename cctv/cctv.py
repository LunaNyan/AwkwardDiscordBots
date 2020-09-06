#!/usr/bin/python3

# ----- CONFIGURATION -----
bot_token = "" # Discord Bot Token
ban_keyword = ["foo", "bar"] # Keyword to detect and ban the user
also_ban_bot = False # also ban bots who says that word
# -------------------------

import discord

@client.event
async def on_message(message):
	if ban_keyword in message.content:
        if not message.author.bot and also_ban_bot:
            await message.author.ban()

client.run(bot_token)