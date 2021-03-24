# bot.py
import os
import random
import discord
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#random qouotes

@bot.command(name='kurwa', help='RAndom Lokkel quote')
async def nine_nine(ctx):

    quotes = [
        'Kackbratze',
        'Kurwa',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(quotes)
    await ctx.send(response)

#roll dice

@bot.command(name='roll_dice', help='Simulates rolling dice. &roll_dice "number of dice"+"number of sides"')
async def roll(ctx, number_of_dice: int, number_of_sides: int):

    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

#create channel

@bot.command(name='create-channel', help='command + txt channel name')
@commands.has_role('staff')
async def create_channel(ctx, channel_name='snekfun'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

#errorr

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')



#reapeter

@bot.command(name='repeat')
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

#joined

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))



bot.run(TOKEN)
