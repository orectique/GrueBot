import discord
import os
import numpy

client = discord.Client()

@client.event
async def on_ready():
    print('Bot is ready')

People = {}

def ngbr():
    for key, value in People[guild]:


def quiz(person):
    tag = '''Hello' + str(person.name) + ', just a few questions.
    
    On a scale of 1-10,
    1. how sociable are you?
    2. how easy is it for you to start a conversation
    
    '''
    person.send(tag)





@client.event
async def on_message(message):

    global People, ngbr, quiz

    person = message.author
    guild = message.guild.id

    if guild not in People:
        People[guild] = {
            guild :{}}
    
    if person not in People[guild]:
        People[guild] = {
            person : []
        }

    if message.author == client.user:
        return

    if message.content.startswith('-GrueMe'):
        if len(People[guild].keys) < 10:
            return await message.channel.send('Not enough members have signed up.')

        friends = ngbr(person)

        tag = str(friends[0].name) + ', ' + str(friends[1]) + ', ' + str(friends[2].name) + ', ' + str(friends[3].name) + ', and ' + str(friends[4].name) + ' have been matched to be your friends!'
        await person.send(tag)

        for friend in friends:
            tag = str(person.name) + ' matched with you!'
            await friend.send(tag)


    if message.content.startswith('-GrueSome'):
        quiz(person)
        await person.send('Your responses have been noted. We\'ll let you know when we find someone.')


       


TOKEN = os.getenv("TOKEN")
client.run(TOKEN)
