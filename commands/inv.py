"""
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

import util.dbf as dbf
import discord

from util.getEmoji import *
# from getEmoji import gold_emoji
from util.makeuser import *

cwd = os.getcwd()


async def inv(message:discord.Message):
    user_id = message.author.id
    if not dbf.doesUserExist(user_id):
        await makeuser(message)
        return
    inv_embed = discord.Embed(title="Inventory")

    inv_filepath = cwd + "/images/icons/Inventory.png"
    inv_file = discord.File(inv_filepath, filename="Inventory.png")
    inv_embed.set_thumbnail(url='attachment://Inventory.png')

    inventory = dbf.getInventory(user_id)
    basket = dbf.getBasket(user_id)
    gold = dbf.getGold(user_id)
    inv_embed.add_field(name=gold_emoji, value=gold, inline=False)
    for entry in inventory:
        name = dbf.getItemNameById(entry[1])
        value = entry[2]
        if value == 0:
            continue
        emoji_name = str(name).replace(" ", "").replace(
            "-", "").replace("_", "").replace("(", "").replace(")", "")
        emojistr = await getEmoji(emoji_name)
        inv_embed.add_field(name=emojistr, value=value, inline=True)
    for entry in basket:
        name = dbf.getCatchableNameById(entry[1])
        value = entry[2]
        if value == 0:
            continue
        emoji_name = str(name).replace(" ", "").replace(
            "-", "").replace("_", "").replace("(", "").replace(")", "")
        emojistr = await getEmoji(emoji_name)
        inv_embed.add_field(name=emojistr, value=value, inline=True)
    await message.reply(embed=inv_embed, file=inv_file)
