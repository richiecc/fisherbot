import nextcord
import dbf
debug = True
async def makeuser(message):
    '''creates user given the message. call this AFTER checking the database PLEASE GOD PLEASE
    this is just a basic function so dont make it difficult...'''
    user_id = message.author.id
    welcome_embed = nextcord.Embed(title="Welcome!", description=str(
        message.author.name) + ", you have been given a **Basic Rod** to start `f`ishing.")
    dbf.insertNewUser(user_id)
    await message.reply(embed=welcome_embed)
    if debug:
        print("made user", user_id)
