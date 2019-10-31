#!/usr/bin/env python3

import discord
import logging
import os
import re
import roll


client = discord.Client()
re_str: str = r'(?P<num>\d+)[Dd]{1}(?P<sides>\d+) (?P<qualifiers>[0-9\+\- ]*)'
regex: str = re.compile(re_str)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# TODO change how it responds to messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!d') or message.content.startswith('!diceman'):
        await message.channel.send('Hello!')

def get_secrets(file: str = 'secret.txt') -> str:
    '''
    Reads the secrets file for the discord client
    '''
    secret: str = ""
    try:
        with open(file, 'r') as s_file:
            secret = s_file.readline()
        return secret
    
    except FileNotFoundError:
        logging.error(
            "diceman.py:get_secrets - Secrets file can not be found or you do not have permissions to read it"
        )
        exit(1) 

def main():

    token: str = ""

    try:
        token = os.environ['DICEMAN_TOKEN']
    except KeyError:
        logging.warning(
            "diceman.py:__main__ - DICEMAN_TOKEN environment variable not set"
        )

    # If token environment variable is not set, look for a token file
    if token != "":
        client.run(token)
    else:
        client.run(get_secrets())




# end main


if __name__ == '__main__':
    main()
