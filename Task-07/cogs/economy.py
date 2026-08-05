import time
import random
import discord 

from discord.ext import commands
from database import (check_balance, get_last_sail, give_sail_reward,trade_berries,get_richest_users )



class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bounty(self, ctx):
        user_id = ctx.author.id

        wallet, bank = check_balance(user_id)
        total = wallet + bank

        await ctx.send(
            f"**{ctx.author.display_name}'s Bounty**\n"
            f"Wallet: {wallet} Berries\n"
            f"Bank: {bank} Berries\n"
            f"Total: {total} Berries"
        )
        
    @commands.command()
    async def setsail(self, ctx):
        user_id = ctx.author.id

        current_time = int(time.time())
        last_sail = get_last_sail(user_id)

        seconds_passed = current_time - last_sail
        one_day = 24 * 60 * 60

        if seconds_passed < one_day:
            seconds_left = one_day - seconds_passed
            hours_left = seconds_left // 3600
            minutes_left = (seconds_left % 3600) // 60

            await ctx.send(
                f"You have already sailed today!\n"
                f"Try again in {hours_left} hours and {minutes_left} minutes."
            )
            return

        reward = random.randint(500, 1000)

        give_sail_reward(user_id, reward, current_time)

        await ctx.send(
            f"⛵ **{ctx.author.display_name} set sail and found treasure!**\n"
            f"You earned **{reward} Berries**."
        )
    @commands.command()
    async def trade(self, ctx, receiver: discord.Member, amount: int):
        sender = ctx.author

        if receiver.id == sender.id:
            await ctx.send("You cannot trade Berries with yourself.")
            return

        if receiver.bot:
            await ctx.send("You cannot trade Berries with a bot.")
            return

        if amount <= 0:
            await ctx.send("Trade amount must be greater than 0.")
            return

        trade_done = trade_berries(
            sender.id,
            receiver.id,
            amount
        )

        if not trade_done:
            await ctx.send("You do not have enough Berries.")
            return

        await ctx.send(
            f"💰 **{sender.display_name}** traded "
            f"**{amount} Berries** with **{receiver.display_name}**."
        )

    @commands.command()
    async def worstgeneration(self, ctx):
        richest_users = get_richest_users()

        if not richest_users:
            await ctx.send("The leaderboard is empty.")
            return

        message = "**🏴‍☠️ The Worst Generation 🏴‍☠️**\n\n"

        place = 1

        for user_id, total_money in richest_users:
            message += (
                f"**{place}.** <@{user_id}> — "
                f"**{total_money} Berries**\n"
            )

            place += 1

        await ctx.send(message,allowed_mentions=discord.AllowedMentions.none())

    @commands.command()
    async def raid(self, ctx, target: discord.Member):
        raider = ctx.author

        if target.id == raider.id:
            await ctx.send("You cannot raid yourself.")
            return

        if target.bot:
            await ctx.send("You cannot raid a bot.")
            return

        target_wallet, target_bank = check_balance(target.id)

        if target_wallet < 200:
            await ctx.send(
                f"{target.display_name} does not have enough Berries to raid."
            )
            return

        raid_won = random.choice([True, False])

        if raid_won:
            smallest_amount = 50
            biggest_amount = max(50, target_wallet // 4)

            stolen = random.randint(smallest_amount,biggest_amount)

            trade_berries(target.id,raider.id,stolen)

            await ctx.send(
                f"🏴‍☠️ **{raider.display_name} successfully raided "
                f"{target.display_name}!**\n"
                f"You stole **{stolen} Berries**."
            )

        else:
            await ctx.send(
                f"❌ **{raider.display_name}'s raid failed!**\n"
                f"{target.display_name} protected their Berries."
            )

async def setup(bot):
    await bot.add_cog(Economy(bot))
