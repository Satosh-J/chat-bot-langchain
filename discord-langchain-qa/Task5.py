import discord
from discord.ext import commands
import openai
from langchain import LangChain

openai.api_key = "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"

# chain = LangChain("gpt-3.5-turbo")

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = commands.Bot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print("Logged in as".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Process the user's message
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.content,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )

    # Send the response back to the user
    await message.channel.send(f'Hello {response.choices[0].text}!')

    await client.process_commands(message)


def get_name_joke(name):
    # Function to generate a joke about the user's name
    return f"Why did {name} go to the store? To buy some new jokes!"


client.run("MTEyOTA2NDc5NzcwMzUxMjE1NQ.GGtwH5.JeqV7Plq-7N9GrpeAXvXOXK0x4W87sOT0E27Xg")