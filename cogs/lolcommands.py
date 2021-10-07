import discord
from discord import file
from discord.ext import commands
from riotapi import *


class summoner_info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    # adds summoner to the bot data
    async def register(self, ctx, *, summoner):
        if summoner not in summoner_names:

            file = discord.File('pics/thumbs_up.png', filename='image.png')

            register_summoner(summoner)

            embed = discord.Embed(
                colour=discord.Color.blue()
            )
            embed.set_author(
                name=ctx.author.display_name,
                icon_url=ctx.author.avatar_url
            )
            embed.add_field(
                name='Register Summoner',
                value=f'{visible_summoner_names[-1]} has been registered.')
            embed.set_image(
                url='attachment://image.png'
            )

            await ctx.send(file=file, embed=embed)
        else:
            await ctx.send(f'{summoner} is aleady registered')

    @commands.command()
    # shows stats of the summoner
    async def stats(self, ctx, *, summoner):
        if summoner in summoner_names:

            file = discord.File('pics/ranked_stats.gif', filename='image.gif')
            print_stats(summoner)

            embed = discord.Embed(
                colour=discord.Color.blue()
            )
            embed.add_field(
                name='Ranked Stats',
                value='\n'.join(visible_stats)
            )
            embed.set_image(
                url='attachment://image.gif'
            )

            await ctx.send(file=file, embed=embed)
            visible_stats.clear()
        else:
            await ctx.send('The summoner is not registered')

    @commands.command()
    # shows available chests
    async def chest(self, ctx, *, summoner):
        if summoner in summoner_names:
            hextech_chest(summoner)
            await ctx.author.send(', '.join(available_chests))

            # for teminal
            print('champion id list has been cleared')
            print('available chests list has been cleared')
            available_chests.clear()
        else:
            await ctx.send('The summoner is not registered')


def setup(client):
    client.add_cog(summoner_info(client))
