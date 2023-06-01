import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot está pronto!')

@bot.command()
async def saldo(ctx):
    await ctx.send("Seu saldo é de X créditos.")  # Exemplo de resposta do bot

@bot.event
async def on_disconnect():
    await bot.close()

bot.run('TOKEN_DO_BOT')
