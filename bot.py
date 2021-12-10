import nextcord
from nextcord.ext import commands
from nextcord.errors import Forbidden

import dbf
import os

'''
main bot script.
careful here, it's the front-end of the true back-end
'''

# if i dont remove the token in a commit, i changed it so dont worry.
token = [
    "no thanks bro"
]

debug = True
cwd = os.getcwd()
client = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


'''
# print updated emoji array for database
async def print_emoji_list():
    await client.wait_until_ready()
    # guild (server) ID with the emotes
    emojis_list = await client.fetch_guild(916321096666599465)
    emojis_list = await emojis_list.fetch_emojis()
    print("emojis_list = [")
    for elem in emojis_list:
        print("(\"" + elem.name + "\"," + str(elem.id) + "\"),")
    print("]")
'''
# EMOJIS FOR BOT TO USE. DO NOT CHANGE. USE ABOVE SCRIPT TO UPDATE VIA STDOUT IF YOU NEED.
# CALL IT WITH A BOT FUNCTION
emojis_list = emojis_list = [

    ("Anemone",                 916323453781565521),
    ("BlackTang",               916323511545511968),
    ("BlueDory",                916323585864372265),
    ("BlueTang",                916323612263325787),
    ("Boots",                   916323666235654174),
    ("BrokenGlass",             916323687811145768),
    ("Butterflyfish",           916323708858142741),
    ("Carrot",                  916323731490631691),
    ("Cichlid",                 916323749786173481),
    ("Clownfish",               916323788881297438),
    ("Cod",                     916323808019902465),
    ("CottonCandyBetta",        916323829171769374),
    ("Dottyback",               916323852655673344),
    ("EmperorRedSnapper",       916323874889674752),
    ("Goatfish",                916323907831734273),
    ("MoorishIdol",             916323932515237888),
    ("OrnateButterfly",         916323953809711154),
    ("Parrotfish",              916323976630923305),
    ("Pogfish",                 916323997644374037),
    ("Pufferfish",              916324016850083881),
    ("QueenAngelfish",          916324038681460776),
    ("RedCichlid",              916324092632764436),
    ("RedLippedBlenny",         916324133330116668),
    ("RedSnapper",              916324157208297532),
    ("Salmon",                  916324181430399037),
    ("Seaweed",                 916324204561960981),
    ("Stick",                   916324226359779399),
    ("Threadfin",               916324248333725717),
    ("TomatoClown",             916324270353842197),
    ("TomatoClownfish",         916324292751401000),
    ("Triggerfish",             916324313630670899),
    ("TropicalFishPreviewgr",   916324335763996712),
    ("TropicalFishPrevieww",    916324369729470464),
    ("WhiteGrayDasher",         916324395125985280),
    ("WhiteSilverSunStreak",    916324424926527570),
    ("YellowtailParrot",        916324448787898388),
    ("YellowTang",              916324478588436480),
    ("GlowRod",                 916332247735472158),
    ("HeavyRod",                916332274251870278),
    ("LavaRod",                 916332300034252850),
    ("OmniRod",                 916332325971828756),
    ("BasicRod",                916332586706563152)
]
gold_emoji = "<:Coins:917234940230385724>"


async def makeuser(message):
    '''creates user given the message. call tihs AFTER checking the database PLEASE GOD PLEASE
    this is just a basic function so dont make it difficult...'''
    user_id = message.author.id
    welcome_embed = nextcord.Embed(title="Welcome!", description=str(
        message.author.name) + ", you have been given a **Basic Rod** to start `f`ishing.")
    dbf.insertNewUser(user_id)
    await message.channel.send(embed=welcome_embed)
    if debug:
        print("made user", user_id)


# async function to turn an emoji from the list into a properly formatted
# discord emoji
async def getEmoji(emoji_name):
    for emoji in emojis_list:
        if(emoji[0] == emoji_name):
            proper = "<:{0}:{1}>".format(str(emoji[0]), str(emoji[1]))
            return proper


@client.event
async def on_message(message):
    # bots cant use this bot
    if message.author.bot:
        return
    user_id = message.author.id

    # fish for fish
    if message.content == ("f"):
        # add user to db if they dont exist. give them 100 gold as well.
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        if debug:
            print("-----------------------------------------------")
            print("user {0} is fishing".format(user_id))
            print("-----------------------------------------------")
        catchable_id = dbf.rollCatchable(user_id)
        if catchable_id == None:
            await message.channel.send("\⛔ Invalid roll! (contact cook#7167 please)")
            return
        elif catchable_id == "no_rod":
            await message.channel.send("\⛔ You don't have the correct rod to fish in this area!")
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
                catchable_name = dbf.getCatchableNameById(catchable_id)[0]
                if catchable_name == "Broken Glass":
                    catchable_name = "Broken_Glass"
                ext = ".png"
                filename = catchable_name + ext

                filepath = cwd + "/images/catchable/" + filename

                if debug:
                    print(filepath)
                catchable_file = nextcord.File(filepath, filename=filename)
                catchable_embed = nextcord.Embed(title="Caught!", description=str(
                    message.author.name) + ", you caught **" + catchable_name + "**!")
                catchable_embed.set_thumbnail(url='attachment://' + filename)
                await message.channel.send(embed=catchable_embed, file=catchable_file)
        if debug:
            print("-----------------------------------------------")

    # total xp TODO: MAKE EMBED
    if message.content == ("xp"):
        # add user to db if they dont exist. give them 100 gold as well.
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        total_xp = dbf.getXpFromUserId(user_id)
        await message.channel.send("\ℹ️ {0}, you have {1} total xp".format(message.author.name, str(total_xp)))

    # inventory embed
    if message.content == ("inv"):
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
        await message.channel.send(embed=inv_embed, file=inv_file)

    # shop help and embed
    if message.content.startswith("shop"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        shop_embed = nextcord.Embed()

        shop_table = []
        # different shops per rarity
        # common
        if message.content.lower() == ("shop common"):
            shop_embed.title = "Common"
            shop_embed.color = nextcord.Color.light_grey()
            for elem in dbf.getShopTableByRarity("Common"):
                shop_table.append(elem)
        # uncommon
        elif message.content.lower() == ("shop uncommon"):
            shop_embed.title = "Uncommon"
            shop_embed.color = nextcord.Color.green()
            for elem in dbf.getShopTableByRarity("Uncommon"):
                shop_table.append(elem)
        # rare
        elif message.content.lower() == ("shop rare"):
            shop_embed.title = "Rare"
            shop_embed.color = nextcord.Color.blue()
            for elem in dbf.getShopTableByRarity("Rare"):
                shop_table.append(elem)
        # legendary
        elif message.content.lower() == ("shop legendary"):
            shop_embed.title = "Legendary"
            shop_embed.color = nextcord.Color.gold()
            for elem in dbf.getShopTableByRarity("Legendary"):
                shop_table.append(elem)
        # unique
        elif message.content.lower() == ("shop unique"):
            shop_embed.title = "Unique"
            shop_embed.color = nextcord.Color.purple()
            for elem in dbf.getShopTableByRarity("Unique"):
                shop_table.append(elem)
        else:
            shop_embed.title = "Shops"
            shop_embed.color = nextcord.Color.blurple()

        if not shop_table == []:
            # for each entry in the shop table, build the embed
            for entry in shop_table:
                item_name = entry[0]
                item_price = entry[1]
                emoji_name = str(item_name).replace(" ", "").replace(
                    "-", "").replace("_", "").replace("(", "").replace(")", "")
                emojistr = await getEmoji(emoji_name)
                shop_embed.add_field(
                    name="{0} {1}".format(item_name, emojistr), value="{0} {1}".format(gold_emoji, item_price), inline=True)
        else:
            shop_embed.add_field(name="shop common",
                                 value="displays common fish and their sell values", inline=False)
            shop_embed.add_field(name="shop uncommon",
                                 value="displays uncommon fish and their sell values", inline=False)
            shop_embed.add_field(
                name="shop rare", value="displays rare fish and their sell values", inline=False)
            shop_embed.add_field(name="shop legendary",
                                 value="displays legendary fish and their sell values", inline=False)
            shop_embed.add_field(name="shop unique",
                                 value="displays unique fish and their sell values", inline=False)
        await message.channel.send(embed=shop_embed)

    # sell items from inventory
    if message.content.startswith("sell"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        # how to
        if message.content == ("sell"):
            sell_help_embed = nextcord.Embed(title="Selling Items")
            sell_help_embed.color = nextcord.Color.blurple()
            sell_help_embed.add_field(
                name="sell all", value="sells all fish and junk", inline=False)
            sell_help_embed.add_field(
                name="sell fish", value="sells all fish and only fish", inline=False)
            sell_help_embed.add_field(
                name="sell junk", value="sells all junk and only junk", inline=False)
            sell_help_embed.add_field(
                name="sell <amount> <item>", value="sells a user-specified amount of an item. the item name is **case-sensitive**")
            await message.channel.send(embed=sell_help_embed)
            return
        # sell only fish
        if message.content == ("sell fish"):
            total_gold_made = 0
            basket = dbf.getBasket(user_id)
            print(basket)
            for elem in basket:
                fish_id = elem[1]
                num_fish = elem[2]
                if num_fish == 0:
                    continue
                value = dbf.getCatchableValueById(fish_id)
                if value == None:
                    continue
                amount_made = value * num_fish
                total_gold_made += amount_made
                dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
            if total_gold_made == 0:
                await message.channel.send("\⛔ {0}, you don't have any fish to sell.".format(message.author.name))
                return
            else:
                dbf.giveGold(user_id, total_gold_made)
                await message.channel.send("\✅ {0} sold all fish for a total of {1} {2}".format(message.author.name, gold_emoji, total_gold_made))
                return

        # sell only junk
        elif message.content == ("sell junk"):
            junk_sold = 0
            basket = dbf.getBasket(user_id)
            print(basket)
            for elem in basket:
                fish_id = elem[1]
                num_fish = elem[2]
                if num_fish == 0:
                    continue
                value = dbf.getCatchableValueById(fish_id)
                if value == None:
                    dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
                    junk_sold += 1
                else:
                    continue
            if junk_sold == 0:
                await message.channel.send("\⛔ {0}, you don't have any junk to sell.".format(message.author.name))
                return
            else:
                await message.channel.send("\✅ {0} sold all junk items for {2} 0".format(message.author.name, junk_sold, gold_emoji))
                return

        # sell everything
        elif message.content == ("sell all"):
            total_gold_made = 0
            junk_sold = 0
            fish_sold = 0
            basket = dbf.getBasket(user_id)
            print(basket)
            for elem in basket:
                fish_id = elem[1]
                num_fish = elem[2]
                if num_fish == 0:
                    continue
                value = dbf.getCatchableValueById(fish_id)
                if value == None:
                    dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
                    junk_sold += 1
                    continue
                amount_made = value * num_fish
                total_gold_made += amount_made
                fish_sold += 1
                dbf.giveUserCatchable(user_id, fish_id, (num_fish * -1))
            if fish_sold == junk_sold == 0:
                await message.channel.send("\⛔ {0}, you don't have anything to sell.".format(message.author.name))
                return
            else:
                dbf.giveGold(user_id, total_gold_made)
                await message.channel.send("\✅ {0} sold {1} fish and {2} junk for a total of {3} {4}".format(message.author.name, fish_sold, junk_sold, gold_emoji, total_gold_made))
                return

        args = message.content.split(" ")

        if args.__len__() <= 2:
            ######### SELL HELP EMBED #########
            if debug:
                print("less than or equal to 2")
            return
        else:
            try:
                amount = int(args[1])
            except:
                await message.channel.send("\⛔ Improper command formatting. Type `sell` for help.")
                return
            fish = args[2]
            fish_id = dbf.getCatchableIdByName(fish)
            if amount > dbf.getCatchableAmount(user_id, fish_id):
                await message.channel.send(
                    "\⛔ You don't have {0}".format(fish))
                return
            elif amount <= 0:
                await message.channel.send("\⛔ You can't sell {0} fish!?!?".format(amount))
                return
            else:
                emoji_name = str(fish).replace(" ", "").replace(
                    "-", "").replace("_", "").replace("(", "").replace(")", "")
                emojistr = await getEmoji(emoji_name)

                value = dbf.getCatchableValueById(fish_id)
                final_gold_value = (value * amount)

                dbf.giveUserCatchable(user_id, fish_id, (amount * -1))
                dbf.giveGold(user_id, final_gold_value)
                await message.channel.send("\✅ {0} sold {1} {2} for a total of {3} {4}".format(message.author.name, amount, emojistr, gold_emoji, final_gold_value))

    # area help and change
    if message.content.startswith("area"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        current_area = int(dbf.getCurrentArea(user_id))
        if message.content == ("area 1") and current_area != 0:
            dbf.changeArea(user_id, 0)
            await message.channel.send("\✅ {0}, you are now in area 1: {1}".format(message.author.name, dbf.getAreaName(0)))
            return
        if message.content == ("area 2") and current_area != 1:
            await message.channel.send("\✅ {0}, you are now in area 2: {1}".format(message.author.name, dbf.getAreaName(1)))
            dbf.changeArea(user_id, 1)
            return
        if message.content == ("area 3") and current_area != 2:
            await message.channel.send("\✅ {0}, you are now in area 3: {1}".format(message.author.name, dbf.getAreaName(2)))
            dbf.changeArea(user_id, 2)
            return
        if message.content == ("area 4") and current_area != 3:
            await message.channel.send("\✅ {0}, you are now in area 4: {1}".format(message.author.name, dbf.getAreaName(3)))
            dbf.changeArea(user_id, 3)
            return
        if message.content == ("area 5") and current_area != 4:
            await message.channel.send("\✅ {0}, you are now in area 5: {1}".format(message.author.name, dbf.getAreaName(4)))
            dbf.changeArea(user_id, 4)
            return
        else:
            await message.channel.send("\ℹ️ {0}, you are in area {1}: {2}".format(message.author.name, current_area + 1, dbf.getAreaName(current_area)))

    # list rods
    if message.content == ("rods"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        await message.channel.send("\⛔ rods not implemented")

    # list and purchase items
    if message.content == ("buy"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        if message.content == ("buy rod"):
            return
        await message.channel.send("\⛔ buy not implemented")

    # user profile to show off
    if message.content == ("profile"):
        if not dbf.doesUserExist(user_id):
            await makeuser(message)
            return
        await message.channel.send("\⛔ profile not implemented")

client.run(token[0])
