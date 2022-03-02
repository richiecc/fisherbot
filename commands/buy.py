import dbf
from commands.makeuser import *
from commands.getEmoji import * 
# from getEmoji import gold_emoji
async def buy(message,user_id):
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