import discord
import random
from discord import client

token ="" 

intents = discord.Intents.all()
client = discord.Client(intents=intents)

messages = ["https://media.discordapp.net/attachments/922478840356425758/926507839982305340/20211220_162425.jpg", "https://media.discordapp.net/attachments/922478840356425758/926507840221356102/20211220_205819.jpg"]
laseraugen = ["linke","Linke","Sozialismus","sozialismus"]

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user.name}")

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='nach dem rechten'))

    async def on_message(self, message):
            if client.user.mentioned_in(message):
                    await message.channel.send(random.choice(messages))
                    print("Gunnar gesendet")

            [await message.channel.send("https://media.discordapp.net/attachments/922478840356425758/927612779819585626/laseraugenheckerman.png") for word in message.content.split(" ") if word in laseraugen]
    
    async def on_guild_join(self, guild):
        await guild.text_channels[0].send("https://media.discordapp.net/attachments/922478840356425758/929432813374148649/unknown.png")
        print("Neuen Server gejoint!")


client = MyClient()
client.run(token)
