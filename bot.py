import nextcord
from nextcord.ext import commands
from nextcord.errors import Forbidden

import dbf
import os

'''
main bot script.
careful here, it's the front-end of the true back-end
'''
# TOKEN OPTIONS
# pip install python-dotenv # client.run(os.getenv('token'))
# OR
# create bot_token.py & type in: token = ""
import bot_token

# if i dont remove the token in a commit, i changed it so dont worry.
# UPDATE 02/03/2022 - We now utilize a bot_token.py file to store the token.
#token = [
#    ""
#]

debug = True
cwd = os.getcwd()
# yes i know i dont use this wow incredible!!!!!!!!
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


# lets import command functions instead!

from commands.help import *
from commands.makeuser import *
from commands.getEmoji import *
from commands.f import *
from commands.xp import *
from commands.inv import *
from commands.shop import *
from commands.sell import *
from commands.area import *
from commands.rods import *
from commands.buy import *

@client.event
async def on_message(message):
    # bots cant use this bot
    if message.author.bot: return
    user_id = message.author.id

    if message.content == ("help"):
        return await help(message)
    
    # fish for fish
    if message.content == ("f"):
       return await f(message,user_id)
    
    # total xp TODO: MAKE EMBED
    if message.content == ("xp"):
        return await xp(message,user_id)
    
    # inventory embed
    if message.content == ("inv"):
        return await inv(message,user_id)

    # shop help and embed
    if message.content.startswith("shop"):
        return await shop(message,user_id)

    # sell items from inventory
    if message.content.startswith("sell"):
        return await sell(message,user_id)
    
    # area help and change
    if message.content.startswith("area"):
        return await area(message,user_id)

    # list rods
    if message.content == ("rods"):
        return await rods(message,user_id)

    # list and purchase items
    if message.content.startswith("buy"):
        return await buy(message,user_id)

    if message.content == "bal" or message.content == "balance":
        bal = dbf.getGold(message.author.id)
        await message.reply("{0}, your balance is {1} {2}".format(message.author.name, gold_emoji, bal))

    # user profile to show off
    if message.content == ("profile"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        await message.reply("\⛔ profile not implemented")
    if message.content == ("reload"):
        print('test')
        try:
            await message.reply("is it working?")
            await client.reload_extension("commands")
            await message.reply("files reloaded!")
        except Exception as err:
            print(str(err))

#client.run(token[0]) # when importing a discord token, python can't determine whether its a string or an object!
client.run(bot_token.token) # this is much better