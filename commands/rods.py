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


async def rods(message, user_id):
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    rods = dbf.getRods()
    rods_embed = discord.Embed()
    rods_embed = discord.Embed(title="Selling Items")
    rods_embed.color = discord.Colour.from_rgb(139, 69, 19)

    print(rods)
    for rod in rods:
        item_name = rod[0]
        if item_name == "Basic Rod":
            continue
        rarity = rod[1]
        value = rod[2]
        # TODO: REGEX
        emoji_name = str(item_name).replace(" ", "").replace(
            "-", "").replace("_", "").replace("(", "").replace(")", "")
        emojistr = await getEmoji(emoji_name)
        rods_embed.add_field(name="{0} {1}".format(
            item_name, emojistr), value="{0} {1}".format(value, gold_emoji), inline=False)
    await message.channel.send(embed=rods_embed)
