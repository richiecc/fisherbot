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
import dbf
import discord

from commands.getEmoji import *
from commands.makeuser import *


async def shop(message:discord.Message):
    user_id = message.author.id
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)

    shop_embed = discord.Embed()

    shop_table = []
    # different shops per rarity
    # common
    if message.content.lower() == ("shop common"):
        shop_embed.title = "Common"
        shop_embed.color = discord.Color.light_grey()
        for elem in dbf.getShopTableByRarity("Common"):
            shop_table.append(elem)
    # uncommon
    elif message.content.lower() == ("shop uncommon"):
        shop_embed.title = "Uncommon"
        shop_embed.color = discord.Color.green()
        for elem in dbf.getShopTableByRarity("Uncommon"):
            shop_table.append(elem)
    # rare
    elif message.content.lower() == ("shop rare"):
        shop_embed.title = "Rare"
        shop_embed.color = discord.Color.blue()
        for elem in dbf.getShopTableByRarity("Rare"):
            shop_table.append(elem)
    # legendary
    elif message.content.lower() == ("shop legendary"):
        shop_embed.title = "Legendary"
        shop_embed.color = discord.Color.gold()
        for elem in dbf.getShopTableByRarity("Legendary"):
            shop_table.append(elem)
    # unique
    elif message.content.lower() == ("shop unique"):
        shop_embed.title = "Unique"
        shop_embed.color = discord.Color.purple()
        for elem in dbf.getShopTableByRarity("Unique"):
            shop_table.append(elem)
    else:
        shop_embed.title = "Shops"
        shop_embed.color = discord.Color.blurple()

    if not shop_table == []:
        # for each entry in the shop table, build the embed
        for entry in shop_table:
            item_name = entry[0]
            item_price = entry[1]
            emoji_name = str(item_name).replace(" ", "").replace(
                "-", "").replace("_", "").replace("(", "").replace(")", "")
            emojistr = await getEmoji(emoji_name)
            shop_embed.add_field(
                name="{0} {1}".format(item_name, emojistr), value="{0} {1}".format(gold_emoji, item_price), inline=True)
    else:
        shop_embed.add_field(name="shop common",
                             value="displays common fish and their sell values", inline=False)
        shop_embed.add_field(name="shop uncommon",
                             value="displays uncommon fish and their sell values", inline=False)
        shop_embed.add_field(
            name="shop rare", value="displays rare fish and their sell values", inline=False)
        shop_embed.add_field(name="shop legendary",
                             value="displays legendary fish and their sell values", inline=False)
        shop_embed.add_field(name="shop unique",
                             value="displays unique fish and their sell values", inline=False)
    await message.channel.send(embed=shop_embed)
