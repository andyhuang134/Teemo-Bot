import discord
import os
from discord.ext import commands

token = 'ODc0NDYxMTE0NzYxNjEzMzcz.YRHTYA.hTqKfnhI0qtSlPywqzJGQFTuQ_8'
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('bot ready')

# clear dms


@client.command()
async def cleardm(ctx, user: discord.User):
    await ctx.channel.purge(limit=1)
    async for message in user.history():
        if message.author == client.user:
            await message.delete()

# extension functions


@client.command()
async def load(ctx, extension):  # ctx represents the context
    client.load_extension(f'cogs.{extension}')
    print('loaded')


@client.command()
async def unload(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print('unloaded')


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print('reloaded')

# loads all the cog files
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    client.run(token)
