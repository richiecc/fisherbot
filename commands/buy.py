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

from commands.getEmoji import *
from commands.makeuser import *


async def buy(message, user_id):
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    if message.content.startswith("buy rod"):
        arg = message.content[8:]
        rod_name = ""
        value = 0
        rod_id = ""
        print(arg)
        if arg == "":
            await message.reply("\⛔ no rod specified")
            return
        rod_table = dbf.getRodNamesAndValues()
        for rod in rod_table:
            if arg.lower() == "basic rod":
                continue
            elif arg.lower() == rod[0].lower():
                rod_name = rod[0]
                value = rod[1]
                rod_id = dbf.getItemIdByName(arg)
                if dbf.getItemAmount(user_id, rod_id) > 0:
                    await message.reply("\⛔ {0}, you already have the {1}!".format(message.author.name, rod_name))
                else:
                    dbf.giveUserItem(
                        user_id, dbf.getItemIdByName(rod_name), 1)
                    currentgold = dbf.getGold(user_id)
                    if currentgold < value:
                        await message.reply("\⛔ {0}, you need {1} more gold to purchase the {2}".format(message.author.name, (value - currentgold), rod_name))
                        return
                    else:
                        dbf.giveGold(user_id, value * -1)
                        await message.reply("✅ {0} successfully purchased {1} for {2} {3}".format(message.author.name, rod_name, gold_emoji, value))
        return
    else:
        await message.reply("BUY HELP EMBED")
