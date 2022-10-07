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

from util.makeuser import *

cwd = os.getcwd()
debug = True


async def f(message:discord.Message):
    user_id = message.author.id
    # add user to db if they dont exist. give them 100 gold as well.
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    if debug:
        print("-----------------------------------------------")
        print("user {0} is fishing".format(user_id))
        print("-----------------------------------------------")
    catchable_id = dbf.rollCatchable(user_id)
    if catchable_id == None:
        print("INVALID ROLL")
        await message.reply("\⛔ Invalid roll! If you are in Dimensional Rift, it has not been implemented yet. Please switch to the previous area, Outer Space.\nIf you are not in Dimensional Rift, contact me (cook#7167) please.")
        return
    elif catchable_id == "no_rod":
        await message.reply("\⛔ You don't have the correct rod to fish in this area!")
        return
    else:
        return_code = dbf.giveUserCatchable(user_id, catchable_id, 1)
        if return_code == 1:
            if debug:
                print("tried to give negative amount of catchable", catchable_id)
        elif return_code == 0:
            if dbf.getCatchableAttributeById(catchable_id) == ("fish"):
                dbf.incrementFishCaught(user_id)
            if debug:
                print("user has been given catchable", catchable_id)
            dbf.giveXpFromCatchableId(user_id, catchable_id)
            catchable_name = dbf.getCatchableNameById(
                catchable_id)[0].replace(" ", "_")
            ext = ".png"
            filename = catchable_name + ext
            print(filename)
            filepath = cwd + "/images/catchable/" + filename
            if debug:
                print(filepath)
            catchable_file = discord.File(filepath, filename=filename)
            catchable_embed = discord.Embed(title="Caught!", description=str(
                message.author.name) + ", you caught **" + catchable_name.replace("_", " ") + "**!")
            catchable_embed.set_thumbnail(url='attachment://' + filename)
            await message.reply(embed=catchable_embed, file=catchable_file)
    if debug:
        print("-----------------------------------------------")
