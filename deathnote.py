#!/usr/bin/python3

# ----- CONFIGURATION -----
bot_token = "" # Discord Bot Token
channel_id = 0 # Channel ID for ban user
# -------------------------

import discord

@client.event
async def on_message(message):
    if message.channel.id == channel_id:
        if "\n" in message.content:
            ul = message.content.split("\n")
        else:
            ul = [message.content]
        for i in ul:
            if " " in i:
                ui = message.content.split(" ")[0]
                r = message.content.split(" ")[1]
            else:
                ui = i
                r = None
            u = await client.fetch_user(int(ui))
            if u == None:
                m = "User ID " + str(i) + " Not Found"
            else:
                await message.guild.ban(user=u, reason=r)
                m = "successfully banned " + u.name
        await message.channel.send(m)

client.run(bot_token)