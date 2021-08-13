import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('bot ready')


# @client.command()
# async def load(ctx, extension):  # ctx represents the context
#    client.load_extension(f'cogs.{extension}')
#
#
# @client.command()
# async def unload(ctx, extension):
#    client.load_extension(f'cogs.{extension}')
#
#
# @client.command()
# async def reload(ctx, extension):
#    client.unload_extension(f'cogs.{extension}')
#    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.environ['DISCORD_TOKEN'])
