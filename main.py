import discord
from discord.ext import commands, tasks
from keep_alive import keep_alive
import os
from colorama import Fore, Style, init
# Initialize colorama
init()
import json
import config
import datetime
import time
import typing
import asyncio
import random
import sys

sys.stdout.reconfigure(encoding='utf-8')

intents = discord.Intents.all()
prefix = "."
bot = commands.Bot(command_prefix=prefix, intents=intents)




@bot.event
async def on_ready():
  print(f"Logged in as {bot.user.name}")
  print("Bot is ready")
  await bot.tree.sync()
  while True:
    await bot.change_presence(activity=discord.Streaming(
        name='C.S.E Batch -55', url="http://twitch.tv/streamer"))
    await asyncio.sleep(30)  # Change activity every in seconds
    await bot.change_presence(activity=discord.Streaming(
        name='Bot-Dev: shellmonbhai', url="http://twitch.tv/streamer"))
    await asyncio.sleep(30)  # Change activity every in seconds
    await bot.change_presence(activity=discord.Streaming(
        name='Bot-Dev: Ali', url="http://twitch.tv/streamer"))
    await asyncio.sleep(30)  # Change activity every in seconds


  

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  content = message.content.lower()
  if content == "hi" or content == "HI":
    await message.channel.send(f'Hello, {message.author.mention}!')
  elif content == '<@713781852338389003>':
    message = await message.reply(f'**ᴡᴀɪᴛ <@713781852338389003> ᴛᴏ ʀᴇᴘʟʏ!**')
    # Reply with an image and delete after 2 minutes
    file = discord.File("shellmonbhai.bio.link.png")
    message2 = await message.channel.send(f"**ɪꜰ ʏᴏᴜ'ʀᴇ ɪɴ ᴀ ʀᴜꜱʜ, ʏᴏᴜ ᴄᴀɴ ᴇɪᴛʜᴇʀ ꜰᴏʟʟᴏᴡ ᴛʜɪꜱ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇꜱꜱ\nʜɪꜱ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴄᴏɴᴛᴀᴄᴛ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴏʀ ꜱᴄᴀɴ ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇᴅ Qʀ ᴄᴏᴅᴇ.\nhttps://shellmonbhai.bio.link/**", file=file)
    await asyncio.sleep(120)  # Sleep for 2 minutes
    await message2.delete()
  elif content == "<@1129407562643685468>":
    message = await message.reply(f'**ᴡᴀɪᴛ ɴɪɢɢᴀ.🐣!!**')

  elif "<@713781852338389003>" in message.content:
    message = await message.reply("👻")
    await asyncio.sleep(5)
    await message.delete()
  elif content == "hello":
    await message.channel.send(f'HI, {message.author.mention}!')
  
  await bot.process_commands(message)




@bot.event
async def on_member_join(member):
    channel_ids = [1191204119571071099, 1191152398421471432]  # Replace with your channel IDs

    for channel_id in channel_ids:
        channel = bot.get_channel(channel_id)
        if channel:
            message = await channel.send(f'Welcome to the server!😀||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||_____{member.mention}')
            await asyncio.sleep(5)
            await message.delete()
        else:
            print(f'Channel with ID {channel_id} not found or bot does not have access.')


@bot.tree.command()
async def verified(interaction: discord.Interaction):
    # Get the server icon URL
    server_icon_url = interaction.guild.icon.url

    # Creating an embed
    embed = discord.Embed(
        title=":tada: ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ ʏᴏᴜ ᴀʀᴇ ᴠᴇʀɪꜰɪᴇᴅ! :tada:",
        description=":star2:- ``ᴡᴇ'ʀᴇ ᴛʜʀɪʟʟᴇᴅ ᴛᴏ ᴏꜰꜰɪᴄɪᴀʟʟʏ ʀᴇᴄᴏɢɴɪᴢᴇ ʏᴏᴜʀ ᴀᴜᴛʜᴇɴᴛɪᴄɪᴛʏ ᴀɴᴅ ᴘʀᴇꜱᴇɴᴄᴇ ᴡɪᴛʜɪɴ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ. ʏᴏᴜʀ ᴠᴇʀɪꜰɪᴇᴅ ꜱᴛᴀᴛᴜꜱ ɪꜱ ᴀ ᴛᴇꜱᴛᴀᴍᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴄᴏɴᴛʀɪʙᴜᴛɪᴏɴꜱ ᴀɴᴅ ᴄʀᴇᴅɪʙɪʟɪᴛʏ.``:star2:\n\n- :clap: ``ᴀ ʀᴏᴜɴᴅ ᴏꜰ ᴀᴘᴘʟᴀᴜꜱᴇ ꜰᴏʀ ᴀᴄʜɪᴇᴠɪɴɢ ᴛʜɪꜱ ᴍɪʟᴇꜱᴛᴏɴᴇ! ʏᴏᴜʀ ᴅᴇᴅɪᴄᴀᴛɪᴏɴ ᴀɴᴅ ᴄᴏᴍᴍɪᴛᴍᴇɴᴛ ʜᴀᴠᴇ ꜱᴇᴛ ʏᴏᴜ ᴀᴘᴀʀᴛ, ᴀɴᴅ ᴡᴇ'ʀᴇ ᴇxᴄɪᴛᴇᴅ ᴛᴏ ʜᴀᴠᴇ ʏᴏᴜ ᴀꜱ ᴀ ᴠᴇʀɪꜰɪᴇᴅ ᴍᴇᴍʙᴇʀ.``\n\n- :rocket: ``ᴀꜱ ᴀ ᴠᴇʀɪꜰɪᴇᴅ ᴍᴇᴍʙᴇʀ, ʏᴏᴜ ɴᴏᴡ ʜᴀᴠᴇ ᴀᴄᴄᴇꜱꜱ ᴛᴏ ᴇxᴄʟᴜꜱɪᴠᴇ ꜰᴇᴀᴛᴜʀᴇꜱ ᴀɴᴅ ᴏᴘᴘᴏʀᴛᴜɴɪᴛɪᴇꜱ. ᴍᴀᴋᴇ ᴛʜᴇ ᴍᴏꜱᴛ ᴏꜰ ᴛʜɪꜱ ʀᴇᴄᴏɢɴɪᴛɪᴏɴ ᴀɴᴅ ᴄᴏɴᴛɪɴᴜᴇ ꜱʜɪɴɪɴɢ ɪɴ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ.``\n\n- :thumbsup: ``ᴏɴᴄᴇ ᴀɢᴀɪɴ, ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ ᴏɴ ʏᴏᴜʀ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ! ᴡᴇ ʟᴏᴏᴋ ꜰᴏʀᴡᴀʀᴅ ᴛᴏ ꜱᴇᴇɪɴɢ ᴍᴏʀᴇ ᴏꜰ ʏᴏᴜʀ ᴀᴍᴀᴢɪɴɢ ᴄᴏɴᴛʀɪʙᴜᴛɪᴏɴꜱ ᴀɴᴅ ꜱᴜᴄᴄᴇꜱꜱ ɪɴ ᴛʜᴇ ꜰᴜᴛᴜʀᴇ.``\n\n- ``ᴄʜᴇᴇʀꜱ ᴛᴏ ʏᴏᴜʀ ᴡᴇʟʟ-ᴅᴇꜱᴇʀᴠᴇᴅ ᴀᴄᴄᴏᴍᴘʟɪꜱʜᴍᴇɴᴛ!`` :partying_face:\n\n# :link:``ɪɴᴠɪᴛᴇ ʀᴇꜱᴛ ᴏꜰ ʏᴏᴜʀ ʙᴀᴛᴄʜᴍᴀᴛᴇꜱ ᴏʀ ꜰʀɪᴇɴᴅꜱ.``",
        color=0xFF0000  # Red color for the embed
    )

    # Set the server icon as the thumbnail
    if server_icon_url:
        embed.set_thumbnail(url=server_icon_url)
    embed.set_image(url="https://media.discordapp.net/attachments/891991625587384332/1194427309009154189/mario-verification.gif")
    # Sending the embed
    await interaction.response.send_message(embed=embed)


keep_alive()  # Starts a webserver to be pinged.
bot.run(os.getenv('TOKEN'))
