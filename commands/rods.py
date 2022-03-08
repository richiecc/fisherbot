import dbf
import nextcord
from commands.makeuser import *
from commands.getEmoji import *
async def rods(message,user_id):
    if not dbf.doesUserExist(user_id):
        return await makeuser(message)
    rods = dbf.getRods()
    rods_embed = nextcord.Embed()
    rods_embed = nextcord.Embed(title="Selling Items")
    rods_embed.color = nextcord.Colour.from_rgb(139, 69, 19)

    print(rods)
    for rod in rods:
        item_name = rod[0]
        if item_name == "Basic Rod":
            continue
        rarity = rod[1]
        value = rod[2]
        emoji_name = str(item_name).replace(" ", "").replace(
            "-", "").replace("_", "").replace("(", "").replace(")", "")
        emojistr = await getEmoji(emoji_name)
        rods_embed.add_field(name="{0} {1}".format(
            item_name, emojistr), value="{0} {1}".format(value, gold_emoji), inline=False)
    await message.channel.send(embed=rods_embed)