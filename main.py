import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
to = "NzE0MjA1ODc0NzA0NDgyMzc1"
ke = ".XsrSDQ."
n = "xYJQ9jwMnniLzktRKX5HiD487vc"


client.run(to+ke+n)