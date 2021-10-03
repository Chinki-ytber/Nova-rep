import os
import discord
from discord.ext import commands
import random
import datetime
import pytz
from keep_alive import keep_alive

client = discord.Client()

intents = discord.Intents.all()
client = commands.Bot(command_prefix =  commands.when_mentioned_or('>>'), intents=intents )
client.remove_command('help')
              


@client.event
async def on_ready():
    print("bot is online")

    await client.change_presence(status=discord.Status.online, activity=discord.Game('>>help for help'))

@client.event
async def on_member_join(member):
    responses= [f'{member.mention} has arrived!',
                f'Welcome to the server {member.mention}.',
                f'{member.mention}, we are happy that you are here.',
                f'Thanks for joining {member.mention}']


    channel = client.get_channel(<channel-id>) 
    await channel.send(random.choice(responses))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! `{round(client.latency * 1000)}ms`')

@client.command()
async def help(ctx):
  helpembed = discord.Embed(title= "__Help__", description ='```Welcome members in the server```' , color=ctx.author.color)


  await ctx.send(embed=helpembed)

@client.command()
async def developer(ctx):
  Embed = discord.Embed(title= "__Developer__", description='This bot is created by <your-name> ', color=ctx.author.color)

  await ctx.send(embed= Embed)




client.run(api key)
