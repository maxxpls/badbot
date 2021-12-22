'''
import os
import discord
from discord.ext import commands
from discord.utils import get
import random
import requests
import json
import responses

client = discord.Client()

cmd = ('&')

def get_yo_momma():
  response = requests.get('https://api.yomomma.info/')
  json_data = json.loads(response.text)
  joke = json_data['joke']
  return joke

@client.event
async def on_ready():
  print('*yawn* ok ok fine im awake jeez')
  print('i am {0.user}'.format(client) + ' and its time for uh stuff')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content
  if msg.startswith(cmd + 'hi'):
    response = random.choice(responses.hi)
    await message.channel.send(response)
  
  if msg.startswith(cmd + 'yo momma'):
    response = get_yo_momma()
    await message.channel.send(response)

  if msg.startswith(cmd + 'good bot'):
    response = random.choice(responses.thanks) + (' :]')
    await message.channel.send(response)
  
  if msg.startswith(cmd + 'bad bot'):
    response = random.choice(responses.sad_ok) + (' :[')
    await message.channel.send(response)

  if msg.startswith(cmd + 'eat my ass'):
    await message.channel.send('i will gladly eat your ass dm me')

my_secret = os.environ['secret']

client.run(my_secret)
'''