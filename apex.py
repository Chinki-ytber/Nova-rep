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
async def on_message(msg):
  if msg.channel.id == 868049471790014464:
    if client.user == msg.author:
        return

    else :
      if 'Congratulations' in msg.content:
        
        tz = pytz.timezone('Asia/Kolkata')
        win_msg = msg.content[16:].format(msg)
        win_text = win_msg.replace("You","")
        win_date = datetime.datetime.now(tz=tz)
        str_date = str(win_date)
        logEmbed = discord.Embed(title= f'Winner logs ({str_date[0:10]})', description = win_text , color = 0x8565F2)
        logEmbed.set_footer(text= f'At: {str_date[11:16]}')
      

        logs = client.get_channel(874230088969891862)

        await logs.send(embed = logEmbed)


  await client.process_commands(msg)
        
        


@client.event
async def on_ready():
    print("bot is online")

    await client.change_presence(status=discord.Status.online, activity=discord.Game('>>help for help'))

@client.event
async def on_member_join(member):
    responses= [f'{member.mention} has arrived!',
                f'Welcome to the server {member.mention}.',
                f'Dekho wo aa gaya,{member.mention} aa gaya.',
                f'{member.mention}, we are happy that you are here.',
                f'Thanks for joining {member.mention}']


    channel = client.get_channel(623829834690199577) 
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
  Embed = discord.Embed(title= "__Developer__", description='This bot is created by <@434396246157819925> ', color=ctx.author.color)

  await ctx.send(embed= Embed)

@client.command()
async def rule(ctx):
  if ctx.channel.id == 843876628928921630 or 868813235183304715:
    thmbnl = 'https://cdn.discordapp.com/attachments/868813235183304715/873930560362381342/discord-2474808-2056094.png'
    ruleembed = discord.Embed(
      title= 'Platform Rules',
      description = '''• Any breaks of the Discord Terms of Service or Guidelines can result in a ban.

• This includes raiding, planning to raid other servers and/or zoom calls, being under the age limit (13 years of age), DOXing, DDoSing, threats, shock imagery, sharing content that violates other companies' EULAs (such as game cheats, pirated games/movies), etc.

_''',
    color =0x8565F2
    )
    ruleembed.add_field(name='__Platform Guidelines__', value= '[Guidelines](https://discord.com/guidelines)',)

    ruleembed.add_field(name='__Terms of Service__', value= '[Discord ToS](https://discord.com/terms)', inline = True)

    ruleembed.set_thumbnail(url = thmbnl)

    await ctx.send(embed = ruleembed)





my_secret = os.environ['token']

keep_alive()

client.run(my_secret)
