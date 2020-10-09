from utils.embeds import Embeds
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Cogs] Events loaded!')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        ignored = (commands.UserInputError, commands.CommandNotFound)
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            await ctx.send(embed=Embeds.cooldown(h, m, s), delete_after=5)

        elif isinstance(error, commands.CheckFailure):
            await ctx.send(embed=Embeds.failure("You don't have the permissions to run this command!"), delete_after=5)

        else:
            raise error


def setup(client):
    client.add_cog(Events(client))
