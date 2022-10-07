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
import util.dbf as dbf
import discord
from util.makeuser import *
from util.level import *
from util.getEmoji import *


async def profile(message:discord.Message):
    user_id = message.author.id
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    
    profile_embed = discord.Embed()
    profile_embed.color = discord.Color.yellow()
    
    # experience
    comma_formatted_xp = "{:,}".format(int(dbf.getXpFromUserId(user_id)))
    profile_embed.add_field(name="📈 Experience", value=comma_formatted_xp,inline=True)
    
    # level
    user_level = levelFromXP(int(dbf.getXpFromUserId(user_id)))
    profile_embed.add_field(name="👾 Level", value=user_level, inline=True)
    
    # gold
    user_gold = "{:,}".format(int(dbf.getGold(user_id)))
    profile_embed.add_field(name=f"{gold_emoji} Gold", value=user_gold, inline=True)

    # rods unlocked
    rod_emoji_list = []
    user_inventory = dbf.getInventory(user_id)
    for item in user_inventory:
        item_amount = item[2]
        if item_amount == 0:
            continue
        # ??????? TODO: FIX THIS LOL
        rod_emoji = await getEmoji(str(dbf.getItemNameById(item[1])).replace(" ", "").replace("-", "").replace("_", "").replace("(", "").replace(")", ""))
        rod_emoji_list.append(rod_emoji)
    profile_embed.add_field(name="🎣 Rods Unlocked", value=" ".join(rod_emoji_list), inline=True)
    
    # favorite area
    fav_area = dbf.getFavoriteArea(user_id)
    profile_embed.add_field(name="🚧 Favorite Area", value=fav_area, inline=True)

    # rarest fish caught
    rarest_fish_id = dbf.getRarestFishId(user_id)
    if rarest_fish_id == -1:
        profile_embed.add_field(name="Rarest Fish Caught", value="No fish!", inline=True)
    else:
        rarest_fish_name = dbf.getCatchableNameById(rarest_fish_id)
        print(rarest_fish_name)
        # oh the fucking misery
        # TODO: REGEX PLEASE GOD SAVE THIS LINE
        rarest_fish_emoji = await getEmoji(str(rarest_fish_name).replace(" ", "").replace("-", "").replace("_", "").replace("(", "").replace(")", ""))
        rarest_fish_rarity = dbf.getCatchableRarityById(rarest_fish_id)
        profile_embed.add_field(name="Rarest Fish Caught", value=f"{rarest_fish_emoji} {rarest_fish_name} ({rarest_fish_rarity})", inline=True)

    # total fish caught
    comma_formatted_fish_caught = "{:,}".format(int(dbf.getNumFishCaught(user_id)))
    profile_embed.add_field(name="Total fish caught", value=comma_formatted_fish_caught, inline=True)
    
    # user profile picture
    profile_embed.set_thumbnail(url=message.author.avatar.url)
    await message.channel.send(embed=profile_embed)
