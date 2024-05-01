import discord
from discord.ext import commands
from numero_wea import numero_wea
from TestfileWrite import writeOnFile

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def ping(ctx):
    """Answers whit pong"""
    await ctx.send("pong")
@bot.command()
async def ofp(ctx, numero: float):
    res = numero_wea(numero)
    await ctx.send(res)



