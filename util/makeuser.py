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

debug = True


async def makeuser(message):
    '''creates user given the message. call this AFTER checking the database PLEASE GOD PLEASE
    this is just a basic function so dont make it difficult...'''
    user_id = message.author.id
    welcome_embed = discord.Embed(title="Welcome!", description=str(
        message.author.name) + ", you have been given a **Basic Rod** to start `f`ishing.")
    dbf.insertNewUser(user_id)
    await message.reply(embed=welcome_embed)
    if debug:
        print("made user", user_id)
