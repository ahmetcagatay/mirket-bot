import discord
import os
from funcs import *
from discord.utils import get
#region permissions
#manage_roles
#manage_nicknames
#endregion
#region Client
token = os.environ.get('BOT-TOKEN')
intents = discord.Intents().all()
client = discord.Client(intents=intents)
prefix = '.'
test_mirket_guild_id = 759132792226971718
mirket_guild_id = 713328432263725066
#endregion
#region Parameters
registRoles = {
  "class": "Eksik",
  "username": "İsim",
  "introduce": "Kendini Tanıt"
}
#endregion
"""
Komutlar ve açıklamaları
.isim       : Kullanıcının ismini sunucuya uygun şekilde olduğunu kontrol ettikten sonra değiştirir

.rol .al    : Soyadı ekleyen kullanıcılardan "İsim" rolünü alır
.rol .ver   : Soyadı eklemeyen kullanıcılara "İsim" rolü verir
"""



@client.event
async def on_member_update(before,after):
    if before.nick != after.nick:
        role_isim = discord.utils.get(after.guild.roles, name=registRoles["username"])
        isAccepted, feedback = await textIsAccepted(after.nick)
        feedback = "Mirket Kullanıcı adınız değiştirildi.\n" + feedback
        channel = await after.create_dm()
        if(isAccepted and await justFirsCharsIsUpper(after.nick)):
            await after.remove_roles(role_isim)
            await channel.send(":green_circle: "+feedback)
            print("+ "+before.nick+ " -> "+after.nick+": "+feedback)
        else:
            await after.add_roles(role_isim)
            await channel.send(":red_circle: "+feedback)
            print("- "+before.nick+ " -> "+after.nick+": "+feedback)

@client.event
async def on_ready():
    test_mirket = client.get_guild(test_mirket_guild_id)
    mirket = client.get_guild(mirket_guild_id)
    
    for guild in client.guilds:
        print(guild.name)    
    print('We have logged in this servers as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(prefix):
        cmd,ctx = await splitContent(message.content)
        role_isim = discord.utils.get(message.guild.roles, name=registRoles["username"])
        if cmd.startswith("isim"):
            if not ctx.startswith(prefix):
                if (await changeUserNickName(message.author,ctx,message.channel)):
                    await message.author.remove_roles(role_isim)

        elif cmd.startswith("rol"):
            if message.author != message.guild.owner:
                print("Kullanıcı sunucu sahibi değil.") 
                return
            
            else:
                cmd,ctx = await splitContent(ctx)
                guild = client.get_guild(message.guild.id)
                
                if cmd.startswith('ver'):
                    
                    unsurnamedMembers = await getUnsurnamedUserIDs(guild,message.channel,client)
                    await setRoleOfMembers(unsurnamedMembers,role_isim)
                    
                elif cmd.startswith('al'):
                    surnamedMembers = await getSurnamedMembers(role_isim,message.guild)
                    await setRoleOfMembers(surnamedMembers,role_isim,False)

async def splitContent(rawcontent):
    """Discorddan gelen ham mesajı komut ve mesaj olarak ayrıştır
    
    Args:
        rawcontent (str): Ham Mesaj

    Returns:
        \ncmd : Komut
        \nctx : Mesaj
    """
    rawcontent = rawcontent.replace(prefix,"",1)
    cmd = rawcontent.split(" ")[0]
    ctx = rawcontent.replace(cmd,"")[1:]
    return cmd, ctx

client.run(token)