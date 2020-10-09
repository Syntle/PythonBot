import os
import random
import arrow
from utils.embeds import Embeds
import discord
from dotenv import load_dotenv
import logging
from discord.ext import commands
from pathlib import Path

load_dotenv('.env')

intents = discord.Intents.all()

token = os.getenv('TOKEN')

client = commands.Bot(command_prefix='.', case_insensitive=True, intents=intents)

logging.basicConfig(level=logging.INFO)

client.cwd = str(Path(__file__).parents[0])
client.uptime = arrow.utcnow()


@client.event
async def on_ready():
    print(f'Servers    ==    {len(client.guilds)}')
    print(f'Users      ==    {len(set(client.get_all_members()))}')
    print(
        f'Invite     ==    https://discord.com/api/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot')
    print(f'Time       ==    {arrow.now()}')
    print(f'{client.user.display_name} has successfully loaded!')
    await client.change_presence(activity=discord.Game(name=f'Written in Python; built like a Python'))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await client.process_commands(message)

if __name__ == '__main__':
    for file in os.listdir(f'{client.cwd}/cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            client.load_extension(f'cogs.{file[:-3]}')

client.run(token)
