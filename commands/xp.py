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

from util.makeuser import *


async def xp(message:discord.Message):
    user_id = message.author.id
    # add user to db if they dont exist. give them 100 gold as well.
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    total_xp = dbf.getXpFromUserId(user_id)
    await message.reply("\ℹ️ {0}, you have {1} total xp".format(message.author.name, str(total_xp)))
