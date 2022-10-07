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


async def sell(message, user_id):
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    # how to
    if message.content == ("sell"):
        sell_help_embed = discord.Embed(title="Selling Items")
        sell_help_embed.color = discord.Color.blurple()
        sell_help_embed.add_field(
            name="sell all", value="sells all fish and junk", inline=False)
        sell_help_embed.add_field(
            name="sell fish", value="sells all fish and only fish", inline=False)
        sell_help_embed.add_field(
            name="sell junk", value="sells all junk and only junk", inline=False)
        sell_help_embed.add_field(
            name="sell <amount> <item>", value="sells a user-specified amount of an item. the item name is **case-sensitive**")
        await message.reply(embed=sell_help_embed)
        return
    # sell only fish
    if message.content == ("sell fish"):
        total_gold_made = 0
        basket = dbf.getBasket(user_id)
        print(basket)
        for elem in basket:
            fish_id = elem[1]
            num_fish = elem[2]
            if num_fish == 0:
                continue
            value = dbf.getCatchableValueById(fish_id)
            if value == None:
                continue
            amount_made = value * num_fish
            total_gold_made += amount_made
            dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
        if total_gold_made == 0:
            await message.reply("\⛔ {0}, you don't have any fish to sell.".format(message.author.name))
            return
        else:
            dbf.giveGold(user_id, total_gold_made)
            await message.reply("\✅ {0} sold all fish for a total of {1} {2}".format(message.author.name, gold_emoji, total_gold_made))
            return

    # sell only junk
    elif message.content == ("sell junk"):
        junk_sold = 0
        basket = dbf.getBasket(user_id)
        print(basket)
        for elem in basket:
            fish_id = elem[1]
            num_fish = elem[2]
            if num_fish == 0:
                continue
            value = dbf.getCatchableValueById(fish_id)
            if value == None:
                dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
                junk_sold += 1
            else:
                continue
        if junk_sold == 0:
            await message.reply("\⛔ {0}, you don't have any junk to sell.".format(message.author.name))
            return
        else:
            await message.reply("\✅ {0} sold all junk items for {2} 0".format(message.author.name, junk_sold, gold_emoji))
            return

    # sell everything
    elif message.content == ("sell all"):
        total_gold_made = 0
        junk_sold = 0
        fish_sold = 0
        basket = dbf.getBasket(user_id)
        print(basket)
        for elem in basket:
            fish_id = elem[1]
            num_fish = elem[2]
            if num_fish == 0:
                continue
            value = dbf.getCatchableValueById(fish_id)
            if value == None:
                dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
                junk_sold += 1
                continue
            amount_made = value * num_fish
            total_gold_made += amount_made
            fish_sold += 1
            dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
        if fish_sold == junk_sold == 0:
            await message.reply("\⛔ {0}, you don't have anything to sell.".format(message.author.name))
            return
        else:
            dbf.giveGold(user_id, total_gold_made)
            await message.reply("\✅ {0} sold {1} fish and {2} junk for a total of {3} {4}".format(message.author.name, fish_sold, junk_sold, gold_emoji, total_gold_made))
            return

    args = message.content.split(" ")

    if args.__len__() <= 2:
        ######### SELL HELP EMBED #########
        if debug:
            print("less than or equal to 2")
        return
    else:
        try:
            amount = int(args[1])
        except:
            await message.reply("\⛔ Improper command formatting. Type `sell` for help.")
            return
        fish = args[2]
        fish_id = dbf.getCatchableIdByName(fish)
        if amount > dbf.getCatchableAmount(user_id, fish_id):
            await message.reply(
                "\⛔ You don't have {0}".format(fish))
            return
        elif amount <= 0:
            await message.reply("\⛔ You can't sell {0} fish!?!?".format(amount))
            return
        else:
            emoji_name = str(fish).replace(" ", "").replace(
                "-", "").replace("_", "").replace("(", "").replace(")", "")
            emojistr = await getEmoji(emoji_name)

            value = dbf.getCatchableValueById(fish_id)
            final_gold_value = (value * amount)

            dbf.giveUserCatchable(user_id, fish_id, (amount * -1))
            dbf.giveGold(user_id, final_gold_value)
            await message.reply("\✅ {0} sold {1} {2} for a total of {3} {4}".format(message.author.name, amount, emojistr, gold_emoji, final_gold_value))
