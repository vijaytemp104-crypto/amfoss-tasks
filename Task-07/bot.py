import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from database import make_tables
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

class BerryBroker(commands.Bot):
    async def setup_hook(self):
        await self.load_extension("cogs.general")
        await self.load_extension("cogs.economy")
        await self.load_extension("cogs.shop")

bot = BerryBroker(
        command_prefix="!",
        intents=intents
        )

@bot.event
async def on_ready():
    print(f"Berry Broker is online as {bot.user}")


make_tables()
bot.run(TOKEN)

