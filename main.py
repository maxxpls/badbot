import os
from discord.ext import commands
import responses
import random
import stupid_error
import datetime
import requests

bot = commands.Bot(command_prefix='+')
@bot.event
async def on_ready():
  print('BAD BOT')
  msg = random.choice(responses.startup)
  print(msg)


@bot.command()
async def test(ctx):
  print('im working')
  await ctx.send('im working')

@bot.command()
async def hi(ctx):
  ans = random.choice(responses.hi)
  await ctx.send(ans)

@bot.command()
async def say(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def goodbot(ctx):
  ans = random.choice(responses.thanks)
  stupid_error.badbot += 1
  await ctx.send(f"{ans} :] \n i have been good **{stupid_error.badbot}** times")

@bot.command()
async def badbot(ctx):
  ans = random.choice(responses.sad_ok)
  stupid_error.goodbot += 1
  await ctx.send(f"{ans} :[ \n i have been bad **{stupid_error.goodbot}** times")

@bot.command()
async def eatmyass(ctx):
  await ctx.send(f"i would gladly eat your ass {ctx.author.name} dm me ;)")

@bot.command()
async def uup(ctx):
  ans = random.choice(responses.imup)
  await ctx.send(ans)

#?
@bot.command()
async def time(ctx):
    now = datetime.datetime.now().strftime
    english = now('%I:%M')
    print(now)
    print(english)
    await ctx.send(english + "\n disclaimer: this is probably wrong")

@bot.command()
async def catfacts(ctx):
  print("LOADING CAT FACTS.EXE")
  facts = requests.get("https://cat-fact.herokuapp.com/fact")
  if (facts == '<Response [503]>'):
    print('ERROR: UNABLE TO RETRIVE FACTS')

  await ctx.send(facts)












  





bot.run(os.environ['secret'])