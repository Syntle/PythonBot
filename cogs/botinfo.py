from datetime import datetime
import discord
from discord.ext import commands


class BotInfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Commands] BotInfo loaded!')

    @commands.command(name='botinfo', description="Display the bot's info", aliases=['stats'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def botinfo(self, ctx):
        embed = discord.Embed(color=discord.Colour.green(),
                              timestamp=datetime.utcnow())
        embed.add_field(name="Created By", value="Syntle", inline=True)
        embed.add_field(name="Servers", value=len(
            self.client.guilds), inline=True)
        embed.add_field(name="Members", value=len(
            set(self.client.get_all_members())), inline=True)
        embed.add_field(
            name="Uptime", value=self.client.uptime.humanize(), inline=True)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(BotInfo(client))
