import discord
from discord.ext import commands
from riotapi import *


class summoner_info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def register(self, ctx, *, arg):

        register_summoner(arg)

        await ctx.send(f'{visible_summoner_names[-1]} has been registered.')

    @commands.command()
    async def stats(self, ctx, *, arg):
        if arg in summoner_names:
            print_stats(arg)
            await ctx.send('\n'.join(visible_stats))
            visible_stats.clear()
        else:
            await ctx.send('The summoner is not registered')

    @commands.command()
    async def chest(self, ctx, arg):
        if arg in summoner_names:
            hextech_chest(arg)
            await ctx.send(available_chests)
            available_chests.clear()
        else:
            await ctx.send('The summoner is not registered')


def setup(client):
    client.add_cog(summoner_info(client))
