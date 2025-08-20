import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import datetime
import asyncio

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

waitTime = datetime.timedelta(hours=4).total_seconds()
startTime = 0
endTime = 4

morningPill = 0
afternoonPill = 2
eveningPill = 3



@bot.event
async def on_ready():
    print('Bot online')

@bot.command()
async def pain(ctx):
    for counter in range(startTime, endTime):
        reply_message = "Record your current pain level"
        embed = discord.Embed(title='Pain Level', description='What is your pain level?')
        poll_message = await ctx.send(embed=embed)
        await poll_message.add_reaction("0️⃣")
        await poll_message.add_reaction("1️⃣")
        await poll_message.add_reaction("2️⃣")
        await poll_message.add_reaction("3️⃣")
        await poll_message.add_reaction("4️⃣")
        await poll_message.add_reaction("5️⃣")
        await poll_message.add_reaction("6️⃣")
        await poll_message.add_reaction("7️⃣")
        await poll_message.add_reaction("8️⃣")
        await poll_message.add_reaction("9️⃣")
        await poll_message.add_reaction("🔟")
        if counter == morningPill:
            await ctx.reply(reply_message + " and take your first pill if you haven't")
        elif counter == afternoonPill:
            await ctx.reply(reply_message + " and take your next pill")
        elif counter == eveningPill:
            await  ctx.reply(reply_message + " and take your last pill")
        else:
            await ctx.reply(reply_message)
        await asyncio.sleep(waitTime)


bot.run(token, log_handler=handler, log_level=logging.DEBUG)