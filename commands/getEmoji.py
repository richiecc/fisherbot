
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
# async function to turn an emoji from the list into a properly formatted
# discord emoji
async def getEmoji(emoji_name):
    for emoji in emojis_list:
        if(emoji[0] == emoji_name):
            proper = "<:{0}:{1}>".format(str(emoji[0]), str(emoji[1]))
            return proper