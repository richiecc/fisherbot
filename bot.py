"""
main bot script.
careful here, it's the front-end of the true back-end

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import os

import discord
from discord.ext import commands

import bot_token
# database functions
import util.dbf as dbf
# bot commands
from commands.area import *
from commands.buy import *
from commands.f import *
from util.getEmoji import *
from commands.help import *
from commands.inv import *
from util.makeuser import *
from commands.profile import *
from commands.rods import *
from commands.sell import *
from commands.shop import *
from commands.xp import *

intents = discord.Intents.default()
intents.message_content = True
debug = True
cwd = os.getcwd()
# yes i know i dont use this wow incredible!!!!!!!!
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message:discord.Message):
    # bots cant use this bot
    if message.author.bot:
        return
    user_id = message.author.id

    if message.content == ("help"):
        return await help(message)

    # fish for fish
    if message.content == ("f"):
        return await f(message)

    # total xp TODO: MAKE EMBED
    if message.content == ("xp"):
        return await xp(message)

    # inventory embed
    if message.content == ("inv"):
        return await inv(message)

    # shop help and embed
    if message.content.startswith("shop"):
        return await shop(message)

    # sell items from inventory
    if message.content.startswith("sell"):
        return await sell(message)

    # area help and change
    if message.content.startswith("area"):
        return await area(message)

    # list rods
    if message.content == ("rods"):
        return await rods(message)

    # list and purchase items
    if message.content.startswith("buy"):
        return await buy(message)

    if message.content == "bal" or message.content == "balance":
        bal = dbf.getGold(message.author.id)
        await message.reply("{0}, your balance is {1} {2}".format(message.author.name, gold_emoji, bal))

    # user profile to show off
    if message.content.lower() == ("profile"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        return await profile(message)

client.run(bot_token.token)
