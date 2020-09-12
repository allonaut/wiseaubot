# tommybot.py
import os
import random

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('oh hi mark')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    tommy_quotes = [
        "Oh hi Mark",
        "Don't touch me motherfucker!",
        "I'm so happy to have you as my best friend, and I love Lisa so much",
        "I did not hit her, it's not true! It's bullshit, I did not hit her, I did naaaaaaht",
        "Johnny's my best friend!",
        "Ha ha ha. What a story Mark!",
        "Hi doggy",
        "Anyway, how's your sex life?",
        "In a few minutes BITCH",
        "Everybody betrayed meeee",
        "I FED UP WITH THIS WUUURHHLD",
        "You're just a chicken. cheeeeep cheep cheep cheep",
        "cheep cheep cheep cheep",
        "YOU ARE TEARING ME APART LISA",
        "The bank saves money and they are using me",
        "You are my rose, you are my rose, you are my rooooose",
        "You think about everything, ha ha ha",
        "Nah",
        "Two is great, but three is a crowd. ha ha ha",
        "That son of a bitch told me I will get it within three months, I saved them bundles, they're crazy, I don't think I'll ever get it. They betrayed me, they didn't keep their promise, they tricked me, and I don't care anymore",
        "AAAAAAFSSTYHGGGGDKDASLSIUR890ZCNBBDFDKHUACNCQ11!!!!!!!!!!!!!!!NNFAUVUYR78AHOJNCBMZKZIUCHAUSQKKLLMCVNVV138JDAM!!!!!!!!!!JKLB"
    ]

    if message.content == 'cheep':
        response = random.choice(tommy_quotes)
        await message.channel.send(response)

client.run('TOKEN HERE') # enter your guild token here
