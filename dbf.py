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

import sqlite3
from random import Random
import os

'''
functions created to make the bot script actually readable
because i know how god damn painful it is to read a script
if you don't have the api docs open on the side.

oh, also for convenience. yeah, that.
'''

debug = True
rand = Random()
cwd = os.getcwd()

database_file_location = cwd + "/fisherbot.db"
db = sqlite3.connect(database_file_location)

# ----------------------------------------------------
# ---------------- information queries ---------------
# ----------------------------------------------------


def getUserData(user_id):
    if debug:
        print("querying user data", end=": ")
    result = db.execute(
        "select * from Users where user_id = ?;", (str(user_id),))
    result.fetchall()
    return result


def getCurrentArea(user_id):
    if debug:
        print("getting current area", end=": ")
    result = db.execute(
        "select area_id from Users where user_id= ?;", (str(user_id),))
    result = result.fetchall()
    if result == []:
        return None
    else:
        toReturn = result[0][0]
        if debug:
            print(toReturn)
        return toReturn


def getAreaName(area_id):
    if debug:
        print("getting area name", end=": ")
    result = db.execute(
        "select area_name from Areas where area_id = ?;", (str(area_id),))
    result = result.fetchall()[0][0]
    if debug:
        print(result)
    return result


def getFishFromAreaAndRarity(area_id, rarity):
    result = db.execute("select * from Catchable where area_id = ? and attribute = ? and rarity = ?;",
                        (str(area_id), "fish", str(rarity)))
    result = result.fetchall()
    return result


def getJunk():
    result = db.execute(
        "select * from Catchable where attribute = ?;", ("junk",))
    result = result.fetchall()
    return result


def getAreas():
    result = db.execute("select * from areas;")
    result = result.fetchall()
    return result


def getInventory(user_id):
    result = db.execute(
        "select * from Inventory where user_id = ?;", (str(user_id),))
    result = result.fetchall()
    return result


def getBasket(user_id):
    result = db.execute(
        "select * from Basket where user_id = ?;", (str(user_id),))
    result = result.fetchall()
    return result


def getItemIdByName(item_name):
    result = db.execute(
        "select item_id from Items where item_name = ?;", (str(item_name),))
    result = result.fetchall()
    return result[0][0]


def getItemNameById(item_id):
    result = db.execute(
        "select item_name from Items where item_id = ?;", (str(item_id),))
    result = result.fetchall()
    return result[0]


def getItemAmount(user_id, item_id):
    result = db.execute(
        "select amount from Inventory where user_id = ? and item_id = ?;", (str(user_id), str(item_id)))
    result = result.fetchall()
    if result == []:
        return 0
    else:
        return result[0][0]


def getCatchableById(catchable_id):
    result = db.execute(
        "select catchable_name, rarity, type from Catchable where catchable_id = ?;", (str(catchable_id),))
    result.fetchall()
    return result


def getCatchableNameById(catchable_id):
    result = db.execute(
        "select catchable_name from Catchable where catchable_id = ?;", (str(catchable_id),))
    result = result.fetchall()
    return result[0]


def getXpFromUserId(user_id):
    result = db.execute(
        "select xp from Users where user_id = ?;", (str(user_id),))
    result = result.fetchall()
    return result[0][0]


def getGold(user_id):
    result = db.execute(
        "select gold from Users where user_id = ?", (str(user_id),))
    result = result.fetchall()
    return result[0][0]


def getShopTableByRarity(rarity):
    result = db.execute(
        "select c.catchable_name, s.buy_price, c.rarity from catchable c, shop s where s.catchable_id = c.catchable_id and c.rarity = ?;", (str(rarity),))
    return result.fetchall()


def getCatchableValueById(catchable_id):
    result = db.execute(
        "select buy_price from Shop s, catchable c where c.catchable_id = ? and c.catchable_id = s.catchable_id;", (str(catchable_id),))
    result = result.fetchall()
    if result == []:
        return None
    else:
        return result[0][0]


def getCatchableAmount(user_id, catchable_id):
    result = db.execute(
        "select amount from Basket where user_id = ? and catchable_id = ?;", (str(user_id), str(catchable_id)))
    result = result.fetchall()
    if result == []:
        return 0
    else:
        return result[0][0]


def getCatchableAttributeById(catchable_id):
    result = db.execute(
        "select attribute from Catchable where catchable_id = ?", (str(catchable_id),))
    result = result.fetchall()
    return result[0][0]


def getCatchableIdByName(catchable_name):
    result = db.execute(
        "select catchable_id from catchable where catchable_name = ?", (str(catchable_name),))
    result = result.fetchall()
    if result == []:
        return None
    else:
        return result[0][0]

# ----------------------------------------------------
# ----------------- boolean queries ------------------
# ----------------------------------------------------


def doesUserHaveItem(user_id, item_id):
    result = db.execute(
        "select item_id from Inventory where user_id = ? and item_id = ?;", (str(user_id), str(item_id)))
    result = result.fetchall()
    if result == []:
        return False
    else:
        return True


def doesUserExist(user_id):
    '''returns `True` if the return tuple has a length and `False` if length is 0'''
    if debug:
        print("checking if user exists", end=": ")
    result = db.execute(
        "select user_id from Users where user_id = ?;", (str(user_id),))
    result = result.fetchall()
    if debug:
        print(result)
    if result.__len__() == 0:
        return False
    return True


def doesUserHaveCatchable(user_id, catchable_id):
    result = db.execute("select catchable_id from Basket where user_id = ? and catchable_id = ?;", (str(
        user_id), str(catchable_id)))
    result = result.fetchall()
    if result.__len__() == 0:
        return False
    else:
        return True


# ----------------------------------------------------
# ---------------------- forms -----------------------
# ----------------------------------------------------

def giveGold(user_id, amount):
    db.execute(
        "update users set gold = gold + ? where user_id = ?;", (amount, str(user_id)))
    db.commit()
    if debug:
        print("gave {0} gold to user {1}".format(amount, user_id))


def insertNewUser(user_id):
    '''inserts user into database by `insert into Users values(user_id, 0, 0, 0, 0);`'''
    if debug:
        print("trying to insert user", end=": ")
    try:
        db.execute("insert into Users values (?, ?, ?, ?, ?);",
                   (str(user_id), 0, 0, 0, 0))
        if debug:
            print("inserted", user_id, "into database")
            print("giving Basic_Rod and some gold", end=": ")
        db.execute("insert into inventory values(?, ?, ?);",
                   (str(user_id), 0, 1))
        if debug:
            print("done! there u go bro")
        db.commit()
    except Exception:
        print("FAILED AT insertNewUser")


def giveUserItem(user_id, item_id, amount):
    if amount <= 0:
        return 1
    if debug:
        print("giving user {0} item(s) with id {1}".format(amount, item_id))
    if(doesUserHaveItem(user_id, item_id)):
        db.execute("update inventory set amount = amount + ? where user_id = ? and item_id = ?;",
                   (amount, str(user_id), str(item_id)))
    else:
        db.execute("insert into inventory values(?, ?, ?);",
                   (str(user_id), str(item_id), amount))
    db.commit()
    return 0


def giveUserCatchable(user_id, catchable_id, amount):
    if debug:
        print("giving user {0} catchable(s) with id {1}".format(
            amount, catchable_id))
    if(doesUserHaveCatchable(user_id, catchable_id)):
        db.execute("update basket set amount = amount + ? where user_id = ? and catchable_id = ?;",
                   (amount, str(user_id), str(catchable_id)))
    else:
        db.execute("insert into Basket values(?, ?, ?);",
                   (str(user_id), str(catchable_id), amount))
    db.commit()
    return 0


def giveXpFromCatchableId(user_id, catchable_id):
    xp_from_catchable = db.execute(
        "select xp_on_catch from Catchable where catchable_id = ?;", (str(catchable_id),))
    xp_from_catchable = xp_from_catchable.fetchall()[0][0]
    if debug:
        print("giving xp from catchable {0}".format(catchable_id), end=": ")
    db.execute("update users set xp = xp + ? where user_id = ?;",
               (xp_from_catchable, str(user_id),))
    if debug:
        print("+{0}xp".format(xp_from_catchable))
    db.commit()


def changeArea(user_id, area_id):
    db.execute("update Users set area_id = ? where user_id = ?;",
               (str(area_id), str(user_id)))
    db.commit()
    if debug:
        print("changed area to {0} for {1}".format(str(area_id), str(user_id)))


def incrementFishCaught(user_id):
    db.execute(
        "update Users set fish_caught = fish_caught + 1 where user_id = ?", (str(user_id),))
    print("incremented fish caught for user {0}".format(user_id))
    db.commit()

# NEW FUNCTION


def getRods():
    result = db.execute(
        "select item_name, rarity, value from Items where type = \"rod\";")
    result = result.fetchall()
    return result


def getRodNames():
    result = db.execute("select item_name from Items where type = \"rod\";")
    result = result.fetchall()
    return result[0]


def getRodNamesAndValues():
    result = db.execute(
        "select item_name, value from Items where type = \"rod\";")
    result = result.fetchall()
    if result == []:
        return None
    else:
        return result


# ----------------------------------------------------
# ----------------------- other ----------------------
# ----------------------------------------------------

def rollCatchable(user_id):
    '''not technically a database function, but it's very bulky and belongs here instead of
    the bot script.
    rolls a catchable item based on user's `area_id`. it checks the user's inventory for
    the proper fishing rod if they are in an area that requires one. if everything checks out,
    the function returns the `catchable_id` of the catchable rolled. if the check fails, this
    function returns `None`.'''
    try:
        area_id = int(getCurrentArea(user_id))
    except:
        if debug:
            print("exception when getting current area integer")
        return None
    if doesUserHaveItem(user_id, getItemIdByName("Omni Rod")):
        pass
    else:
        if area_id == 0 and not doesUserHaveItem(user_id, getItemIdByName("Basic Rod")):
            if debug:
                print("no basic")
            return "no_rod"
        elif area_id == 1 and not doesUserHaveItem(user_id, getItemIdByName("Glow Rod")):
            if debug:
                print("no glow")
            return "no_rod"
        elif area_id == 2 and not doesUserHaveItem(user_id, getItemIdByName("Lava Rod")):
            if debug:
                print("no lava")
            return "no_rod"
        elif area_id == 3 and not doesUserHaveItem(user_id, getItemIdByName("Heavy Rod")):
            if debug:
                print("no heavy")
            return "no_rod"
        elif area_id == 4 and not doesUserHaveItem(user_id, getItemIdByName("Omni Rod")):
            if debug:
                print("no omni")
            return "no_rod"
        else:
            pass
    junk = getJunk()
    # here you can set the percentage chance of getting something
    # the base chance is out of 1000 to allow for numbers like 0.001% for super rares and whatnot

    # junk - 10%
    # fish - 90%
    category_integer = rand.randint(1, 1000)  # random integer [1,1000]
    if debug:
        print("category ({0})".format(category_integer), end=": ")
    # [1000, 900)
    if 900 <= category_integer <= 1000:
        if debug:
            print("junk")
        junk_id = junk[rand.randint(0, len(junk)-1)][0]
        return junk_id
    # [900, 1]
    elif 1 <= category_integer < 900:
        if debug:
            print("fish")
        # fish has their own ranges, depending on which area.
        # rarities differ on area. different areas unlock
        # different common fish and different rarities of fish.
        # below is the general rarity table.
        #   ---------------------
        #   | common    |  900  |
        #   | uncommon  |   70  |
        #   | rare      |   25  |
        #   | legendary |    5  |
        #   ---------------------
        # essentially, it's
        # 1 - (uncommon + rare + legendary)
        # for common rarity
        rarity_integer = rand.randint(1, 1000)  # random integer [1,1000]
        if debug:
            print("rarity ({0}): ".format(rarity_integer), end=": ")

        if area_id == 0:
            #   ----- The Ocean -----
            #   | common    | 1000  |
            #   ---------------------
            if debug:
                print("common")
            fish = getFishFromAreaAndRarity(0, "Common")
            fish_id = fish[rand.randint(0, len(fish)-1)][0]
            return fish_id
        elif area_id == 1:
            #   ----- Deep Cave -----
            #   | common    |  930  |
            #   | uncommon  |   70  |
            #   ---------------------
            if 70 < rarity_integer <= 1000:
                print("Common")
                fish = getFishFromAreaAndRarity(1, "Common")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            elif 1 <= rarity_integer <= 70:
                print("Uncommon")
                fish = getFishFromAreaAndRarity(1, "Uncommon")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            else:
                print("broke at area 1")
                return None
        elif area_id == 2:
            #   ----- Lava Pool -----
            #   | common    |  905  |
            #   | uncommon  |   70  |
            #   | rare      |   25  |
            #   ---------------------
            if 95 < rarity_integer <= 1000:
                if debug:
                    print("Common")
                fish = getFishFromAreaAndRarity(2, "Common")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            elif 25 < rarity_integer <= 95:
                if debug:
                    print("Uncommon")
                fish = getFishFromAreaAndRarity(2, "Uncommon")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            elif 1 <= rarity_integer <= 25:
                if debug:
                    print("Rare")
                fish = getFishFromAreaAndRarity(2, "Rare")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            else:
                print("broke at area 2")
                return None
        elif area_id == 3:
            #   ---- Outer Space ----
            #   | common    |  900  |
            #   | uncommon  |   70  |
            #   | rare      |   25  |
            #   | legendary |    5  |
            #   ---------------------
            if 100 < rarity_integer <= 1000:
                if debug:
                    print("Common")
                fish = getFishFromAreaAndRarity(3, "Common")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            elif 30 < rarity_integer <= 100:
                if debug:
                    print("Uncommon")
                fish = getFishFromAreaAndRarity(3, "Uncommon")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            elif 5 < rarity_integer <= 30:
                if debug:
                    print("Rare")
                fish = getFishFromAreaAndRarity(3, "Rare")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            elif 1 <= rarity_integer <= 5:
                if debug:
                    print("Legendary")
                fish = getFishFromAreaAndRarity(3, "Legendary")
                fish_id = fish[rand.randint(0, len(fish)-1)][0]
                return fish_id
            else:
                print("broke at area 3")
                return None
    print(category_integer)
    return
