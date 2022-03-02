import dbf
from commands.makeuser import *
async def xp(message,user_id):
    # add user to db if they dont exist. give them 100 gold as well.
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    total_xp = dbf.getXpFromUserId(user_id)
    await message.reply("\ℹ️ {0}, you have {1} total xp".format(message.author.name, str(total_xp)))