import discord
from discord.utils import get
import asyncio
import inspect

registRoles = {
  "class": "Eksik",
  "username": "İsim",
  "introduce": "Kendini Tanıt"
}



def currentFunction():
    return inspect.stack()[1][3]

async def getDMMessage(situation):
    if situation == "":
        pass

async def textIsAccepted(text):
    alphabet = "abcçdefgğhiıjklmnoöprsştuüvyzABCÇDEFGĞHİIJKLMNOÖPRSŞTUÜVYZ "

    if len(text.split(" ")) > 3:
        return False, "En fazla 3 isim girebilirsiniz."
    elif len(text.split(" ")) < 2:
        return False, "En az 2 isim girmelisiniz."
    elif text[-1] == " ":
        return False, "Lütfen isminizin sonuna boşluk bırakmayınız."
    for word in text:
        if word not in alphabet:
            return False , "Alfabe harfleri dışında bir karakter kabul edilmez."
    for word in text.split(" "):
        if len(word) < 2:
            return False, "İsim içerisinde tek harf kabul edilmez."

    return True, "Tebrikler kullanıcı adınız başarılı bir şekilde kaydedildi."
async def justFirsCharsIsUpper(name):
    for word in name.split(" "):
        for i in range(0,len(word)):
            if i == 0:
                if word[i].islower():
                    return False
            else:
                if word[i].isupper():
                    return False
    return True
async def capitalFirstChars(words):
    capitalizedWords = ""
    for word in words.split(" "):
        capitalizedWords += word.capitalize() + " "
    return capitalizedWords[:-1]

async def getUnsurnamedUserIDs(guild,feedbackChannel,client):
    memberList= []
    for member in guild.members:
        if not member.bot:
            username = member.nick
            if username == None:
                username = member.name
            if " " not in str(username) or not await textIsAccepted(username):
                memberList.append(member)
    return memberList
async def getSurnamedMembers(_role,guild):
    #feedbackChannel işe yaramıyor onu içine koyularsa
    #feedback gönder şeklinde tasarla
    memberList= []
    for member in guild.members:
        if not member.bot:
            for role in member.roles:
                if role.id == _role.id:
                    username = member.nick
                    if username == None:
                        username = member.name
                    if " " in username and await textIsAccepted(username):
                        memberList.append(member)
    return memberList
async def getUserHasRole(roleName,guild):
    memberList= []
    for member in guild.members:
        for role in member.roles: 
            if role.name == roleName:
                memberList.append(member)
    return memberList

async def changeUserNickName(member,newName,feedbackChannel={}):
    """
    Args:
        
        member: (discord.Member)
        newName: (str)
        feedbackChannel: (discord.Message.channel, optional): If you want send feedback to user, you should put the feedbackChannel.
    """
    isAccepted, feedback = await textIsAccepted(newName)
    if isAccepted:
        capitalizedName = await capitalFirstChars(newName)
        await member.edit(nick=capitalizedName)

    if feedbackChannel is not changeUserNickName.__defaults__[0]:
        await feedbackChannel.send(feedback)
    return isAccepted
async def setRoleOfMembers(memberList,role,add=True):
    """[summary]

    Args:

        memberList (array(discord.Member)): Üye listesi

        role (discord.Member.roles): Rol

        add (bool, optional): Rol eklensin mi silinsin mi?. Defaults to True.
    """
    count = 0
    for member in memberList:
        print(count,"Rol:", role.name ,end=" ")
        if add:
            await member.add_roles(role)
            print("+ Eklendi:", end="")
        else:
            await member.remove_roles(role)
            print("- Silindi", end="")
        print("- Kullanıcı:", member.nick) if member.nick != None else print("- Kullanıcı:",member.name)
        count += 1
isim_list=["aynen#5382","wouther#9621","seynan#1931","ruzun#5623","Aggressive#6988","Aşık Barani#9344","m1rex090#1215","Barış#7076","Gregorios#8494","Carathis.#0410","ተ Beysaağ ᵗʰᵉ ᵛᶤᶰᶜᵉᶰᵗ#3189","upss#8729","nefil#1663"]

async def sendMessageMembersRole(role:discord.Role,Message,sleepTime:int=120):
    members = role.members

    count=1
    for member in members:
        print(count,member)
        count+=1
    count=1
    for member in members:
        try:
            channel = await member.create_dm()
            await channel.send(Message)
            print(count, str(member))
            count+=1
            await asyncio.sleep(sleepTime)
        except:
            print("Bir hata oluştu.")