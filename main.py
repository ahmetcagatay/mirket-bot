import discord
import os
import random
import asyncio
import aiohttp
from discord import Game
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands import errors
import time as t

token = os.environ.get('BOT-TOKEN')
#Bot prefix
bot = commands.Bot(command_prefix='.')
role_id = 771647376385507339
role_idtest = 772184494287093781

channel_id = 771647652232036352
channel_test_id = 772184423603896320

@bot.event
async def on_ready():
    print(f'{bot.user.name} artık aktif!')
    print(f'{bot.user.id} sunucuda...')
    await bot.change_presence(activity=discord.Game(name="Mirket"))

@bot.event
async def on_voice_state_update(member, before, after):
    role = discord.utils.get(member.guild.roles, id=role_id)
    role2 = discord.utils.get(member.guild.roles, id=role_idtest)
    if before.channel is None and after.channel is not None:
        if after.channel.id == channel_test_id:
            await member.add_roles(role)
        else:
            await member.remove_roles(role)

    elif before.channel is not None and after.channel is not None:
        if after.channel.id == channel_test_id:
            await member.add_roles(role)
        else:
            await member.remove_roles(role)

    elif before.channel is not None and after.channel is None:
        if before.channel.id == channel_test_id:
            await member.remove_roles(role)
        else:
            pass
    #TEST SERVERI
    elif before.channel is None and after.channel is not None:
        if after.channel.id == channel_test_id:
            await member.add_roles(role2)
        else:
            await member.remove_roles(role2)

    elif before.channel is not None and after.channel is not None:
        if after.channel.id == channel_test_id:
            await member.add_roles(role2)
        else:
            await member.remove_roles(role2)

    elif before.channel is not None and after.channel is None:
        if before.channel.id == channel_test_id:
            await member.remove_roles(role2)
        else:
            pass
    else:
        pass

bot.run(token)
