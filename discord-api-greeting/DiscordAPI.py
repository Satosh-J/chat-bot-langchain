import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # Ignore messages from the bot itself to prevent recursion
    if message.author == client.user:
        return

    # Send greeting message
    await message.channel.send(f'Hello {message.author.name}!')

    # Process commands
    await bot.process_commands(message)


client.run('MTEyOTA2NDc5NzcwMzUxMjE1NQ.GGtwH5.JeqV7Plq-7N9GrpeAXvXOXK0x4W87sOT0E27Xg')

