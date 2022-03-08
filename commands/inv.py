import nextcord
import dbf
from commands.getEmoji import *
# from getEmoji import gold_emoji
from commands.makeuser import *
import os
cwd = os.getcwd()

async def inv(message,user_id):
    if not dbf.doesUserExist(user_id):
        await makeuser(message)
        return
    inv_embed = nextcord.Embed(title="Inventory")

    inv_filepath = cwd + "/images/icons/Inventory.png"
    inv_file = nextcord.File(inv_filepath, filename="Inventory.png")
    inv_embed.set_thumbnail(url='attachment://Inventory.png')

    inventory = dbf.getInventory(user_id)
    basket = dbf.getBasket(user_id)
    gold = dbf.getGold(user_id)
    inv_embed.add_field(name=gold_emoji, value=gold, inline=False)
    for entry in inventory:
        name = dbf.getItemNameById(entry[1])
        value = entry[2]
        if value == 0:
            continue
        emoji_name = str(name[0]).replace(" ", "").replace(
            "-", "").replace("_", "").replace("(", "").replace(")", "")
        emojistr = await getEmoji(emoji_name)
        inv_embed.add_field(name=emojistr, value=value, inline=True)
    for entry in basket:
        name = dbf.getCatchableNameById(entry[1])
        value = entry[2]
        if value == 0:
            continue
        emoji_name = str(name[0]).replace(" ", "").replace(
            "-", "").replace("_", "").replace("(", "").replace(")", "")
        emojistr = await getEmoji(emoji_name)
        inv_embed.add_field(name=emojistr, value=value, inline=True)
    await message.reply(embed=inv_embed, file=inv_file)