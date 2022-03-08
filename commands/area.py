import dbf
from commands.makeuser import *
import nextcord 

async def area(message,user_id):
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    current_area = int(dbf.getCurrentArea(user_id))
    if message.content == ("area 1") and current_area != 0:
        dbf.changeArea(user_id, 0)
        await message.reply("\✅ {0}, you are now in area 1: {1}".format(message.author.name, dbf.getAreaName(0)))
        return
    if message.content == ("area 2") and current_area != 1:
        await message.reply("\✅ {0}, you are now in area 2: {1}".format(message.author.name, dbf.getAreaName(1)))
        dbf.changeArea(user_id, 1)
        return
    if message.content == ("area 3") and current_area != 2:
        await message.reply("\✅ {0}, you are now in area 3: {1}".format(message.author.name, dbf.getAreaName(2)))
        dbf.changeArea(user_id, 2)
        return
    if message.content == ("area 4") and current_area != 3:
        await message.reply("\✅ {0}, you are now in area 4: {1}".format(message.author.name, dbf.getAreaName(3)))
        dbf.changeArea(user_id, 3)
        return
    if message.content == ("area 5") and current_area != 4:
        await message.reply("\✅ {0}, you are now in area 5: {1}".format(message.author.name, dbf.getAreaName(4)))
        dbf.changeArea(user_id, 4)
        return
    else:
        await message.reply("\ℹ️ {0}, you are in area {1}: {2}".format(message.author.name, current_area + 1, dbf.getAreaName(current_area)))