import discord


class Embeds:
    def cooldown(h, m, s):
        description = None

        h = round(h)
        m = round(m)
        s = round(s)

        if int(h) is 0 and int(m) is 0:
            description = f'⏱️ Please wait {s} seconds before trying this command again!'
        elif int(h) is 0 and int(m) is not 0:
            description = f'⏱️ Please wait {m} minutes & {s} seconds before trying this command again!'
        else:
            description = f'⏱️ Please wait {h} hours, {m} minutes & {s} seconds before trying this command again!'\

        embed = discord.Embed(
            description=description,
            color=discord.Colour.red()
        )

        return embed

    def failure(error):
        embed = discord.Embed(
            description=error,
            color=discord.Colour.red()
        )

        return embed
