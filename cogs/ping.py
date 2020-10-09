from os import name
import discord
from discord.ext import commands
import math
from datetime import datetime


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Commands] Ping loaded!')

    @commands.command(name='ping', description='Pings the bot', aliases=['pong'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ping(self, ctx):
        msg = await ctx.send('Pinging...')
        ping = math.floor(datetime.timestamp(
            msg.created_at) - datetime.timestamp(ctx.message.created_at))

        embed = discord.Embed(color=discord.Colour.green())
        embed.add_field(name='Ping', value=f'{ping}ms', inline=True)
        embed.add_field(name='API Ping', value=f'{round(self.client.latency)}ms', inline=True)
        
        await msg.edit(content=None, embed=embed)


def setup(client):
    client.add_cog(Ping(client))
