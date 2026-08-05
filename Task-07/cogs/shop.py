from discord.ext import commands

from items import shop_items
from database import buy_item, get_inventory

class Shop(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx):
        message = "**Berry Broker's Shop**\n\n"

        for item_name, item in shop_items.items():
            message += (
                f"**{item_name.title()}** — {item['price']} Berries\n"
                f"{item['effect']}\n\n"
            )

        await ctx.send(message)

    @commands.command()
    async def buy(self, ctx, *, item_name):
        item_name = item_name.lower()

        if item_name not in shop_items:
            await ctx.send("That item is not available in the shop.")
            return

        item = shop_items[item_name]

        bought = buy_item(
            ctx.author.id,
            item_name,
            item["price"]
        )

        if not bought:
            await ctx.send("You do not have enough Berries.")
            return

        await ctx.send(
            f"You bought **{item_name.title()}** "
            f"for **{item['price']} Berries**."
        )
    @commands.command()
    async def inventory(self, ctx):
        items = get_inventory(ctx.author.id)

        if not items:
            await ctx.send("Your inventory is empty.")
            return

        message = f"**{ctx.author.display_name}'s Inventory**\n\n"

        for item_name, status, quantity in items:
            message += (
                f"**{item_name.title()}** × {quantity} "
                f"— {status.title()}\n"
            )

        await ctx.send(message)


async def setup(bot):
    await bot.add_cog(Shop(bot))
