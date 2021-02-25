import discord
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
isim_mesaj = "**Önemli**\
\nYeni alınan bir karar göre **Mirket Topluluğu** üyelerinin kullanıcı adları **'İsim Soyisim'** şeklinde düzenlemeleri gerekmektedir.\
\nDetaylı açıklama için bakınız -> <#807940631334486048> \
\n:red_circle: Uyarı: İsminizi değiştirmediğiniz takdirde topluluktan uzaklaştırılacaksınız."

"""
Komutlar ve açıklamaları
.rol .mesaj : isim rolünü değiştirmeyen kullanıcılara özelden mesaj gönderir
"""



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
        if cmd.startswith("rol"):
            if message.author != message.guild.owner:
                print("Kullanıcı sunucu sahibi değil.") 
                return
            cmd,ctx = await splitContent(ctx)
            guild = client.get_guild(message.guild.id)
            if cmd.startswith('mesaj'):
                unsurnamedMembers = await getUnsurnamedUserIDs(guild,message.channel,client)
                await sendMessageMembersRole(role_isim, isim_mesaj,60)

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