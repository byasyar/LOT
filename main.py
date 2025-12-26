import discord
import random
from discord import app_commands

class LOT(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            intents=intents 
        )
        self.tree = app_commands.CommandTree(self)
    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print ("Bot  ligado, pode trollar!")

bot = LOT()

@bot.tree.command(name="lane", description="Sorteio da lane")
async def lane(interaction:discord.Interaction):
    messages = ("Top", "Bot", "Sup", "Mid", "Jungle")
    await interaction.response.send_message(random.choice(messages))


bot.run("aaa")
