"""
This cool script lets you create all tables and generate all of the
necessary data for the sqlite3 database required to run the bot properly.
Configure the variables right below this text, if you want.

yes i do understand that it's not proper to have functions containing
basically the same code....... it is what it is. this was faster than
developing a proper system based on rows and bla bla bla. plus custom
shop generation was easier this way too. oh well.

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
import os
import sys
import time
# ---------------------------------------------------------------
# ------------------------- global vars -------------------------
# ---------------------------------------------------------------

# current working directory
cwd = os.getcwd()
# timestamp in case
timestamp = str(round(time.time() * 1000))

# ---------------------------------------------------------------
# ------------------------ configurables ------------------------
# ---------------------------------------------------------------

# drops tables if they exist and commits changes to the database
drop = False

# prints properly formatted SQL script to stdout for command line use, if necessary
# this will remove the debug prints
stdout = True

# outputs properly formatted SQL scripts to files including table drop/create
# (will add option later for single file output)
toFile = False

# overwrites tables that store data IF AND ONLY IF drop is also true.
# YOU CAN USE include_user_data_tables = true AND BE PERFECTLY FINE IF drop = false
# SINCE IT WILL GENERATE SQL FOR TABLES THAT STORE DATA
include_user_data_tables = True


# keep it default please
if drop or include_user_data_tables:
    database_file_location = cwd + "/fisherbot.db"
# ---------------------------------------------------------------
# ------------------------- huge tables -------------------------
# ---------------------------------------------------------------
catchable = [
    # ------------------------ Catchable ------------------------
    # | catchable_id      |   number PRIMARY_KEY unique |   0   |
    # | catchable_name    |   text not null             |   1   |
    # | area_id           |   number not null           |   2   |
    # | xp_on_catch       |   number not null           |   3   |
    # | rarity            |   text not null             |   4   |
    # | attribute         |   text not null             |   5   |
    # -----------------------------------------------------------
    (0,     "Cod",                          0,  5,      "Common",       "fish"),
    (1,     "Salmon",                       0,  7,      "Common",       "fish"),
    (2,     "Pufferfish",                   0,  10,     "Common",       "fish"),
    (3,     "Boots",                        -1, 1,      "Junk",         "junk"),
    (4,     "Broken Glass",                 -1, 1,      "Junk",         "junk"),
    (5,     "Carrot",                       -1, 1,      "Junk",         "junk"),
    (6,     "Seaweed",                      -1, 1,      "Junk",         "junk"),
    (7,     "Stick",                        -1, 1,      "Junk",         "junk"),
    (8,     "Cichlid",                      1,  20,     "Common",       "fish"),
    (9,     "Blue Dory",                    1,  20,     "Common",       "fish"),
    (10,    "Butterflyfish",                1,  20,     "Common",       "fish"),
    (11,    "Triggerfish",                  1,  20,     "Common",       "fish"),
    (12,    "Blue Tang",                    1,  80,     "Uncommon",     "fish"),
    (13,    "Black Tang",                   1,  80,     "Uncommon",     "fish"),
    (14,    "Red-Lipped Blenny",            1,  90,     "Uncommon",     "fish"),
    (15,    "Red Cichlid",                  2,  50,     "Common",       "fish"),
    (16,    "Red Snapper",                  2,  50,     "Common",       "fish"),
    (17,    "Emperor Red Snapper",          2,  75,     "Common",       "fish"),
    (18,    "Tomato Clown",                 2,  50,     "Common",       "fish"),
    (19,    "Tomato Clownfish",             2,  95,     "Uncommon",     "fish"),
    (20,    "Ornate Butterfly",             2,  95,     "Uncommon",     "fish"),
    (21,    "Anemone",                      2,  165,    "Rare",         "fish"),
    (22,    "White-Silver SunStreak",       3,  100,    "Common",       "fish"),
    (23,    "White-Gray Dasher",            3,  100,    "Common",       "fish"),
    (24,    "Moorish Idol",                 3,  100,    "Common",       "fish"),
    (25,    "Threadfin",                    3,  110,    "Common",       "fish"),
    (26,    "Yellow Tang",                  3,  250,    "Uncommon",     "fish"),
    (27,    "Goatfish",                     3,  250,    "Uncommon",     "fish"),
    (28,    "Yellowtail Parrot",            3,  250,    "Uncommon",     "fish"),
    (29,    "Clownfish",                    3,  300,    "Rare",         "fish"),
    (30,    "Tropical Fish Preview (gr)",   3,  2000,   "Legendary",    "fish"),
    (31,    "Tropical Fish Preview (w)",    3,  2000,   "Legendary",    "fish"),
    (32,    "Cotton Candy Betta",           4,  150,    "Common",       "fish"),
    (33,    "Parrotfish",                   4,  275,    "Uncommon",     "fish"),
    (34,    "Queen Angelfish",              4,  350,    "Rare",         "fish"),
    (35,    "Dottyback",                    4,  2500,   "Legendary",    "fish"),
    (36,    "Pogfish",                      4,  12500,  "Unique",       "fish")
]

areas = [
    # -------------------------- Areas --------------------------
    # | area_id           |   number PRIMARY_KEY unique |   0   |
    # | area_name         |   text not null             |   1   |
    # -----------------------------------------------------------
    (0,     "The Ocean"),
    (1,     "Deep Cave"),
    (2,     "Lava Pool"),
    (3,     "Outer Space"),
    (4,     "Dimensional Rift")
]

items = [
    # -------------------------- Items --------------------------
    # | item_id           |   number PRIMARY_KEY unique |   0   |
    # | item_name         |   text not null             |   1   |
    # | rarity            |   text not null             |   2   |
    # | value             |   number default null       |   3   |
    # | type              |   text not null             |   4   |
    # | attribute         |   text default null         |   5   |
    # -----------------------------------------------------------
    (0,     "Basic Rod",        "Common",       0,              "rod",      None),
    (1,     "Glow Rod",         "Uncommon",     500,            "rod",      None),
    (2,     "Lava Rod",         "Rare",         10000,          "rod",      None),
    (3,     "Heavy Rod",        "Legendary",    1000000,        "rod",      None),
    (4,     "Omni Rod",         "Unique",       99999999,       "rod",      None)
]


shop = [
    # --------------------------- Shop --------------------------
    # | catchable_id      |   number PRIMARY_KEY unique |   0   |
    # | buy_price         |   text not null             |   1   |
    # -----------------------------------------------------------
]
# fish gold values generated based on catchables.
# this is generated like this to allow for expandability,
# in case more fish are added or something. who knows.
for c in catchable:
    c_id = c[0]             # catchable ID
    area = c[2]             # area ID
    rarity = c[4]           # rarity
    attribute = c[5]        # attribute (junk/fish)

    rarity_weights = {      # weights of rarity for value calculation
        "Junk": 0,
        "Common": 10,
        "Uncommon": 20,
        "Rare": 45,
        "Legendary": 115,
        "Unique": 300
    }

    attribute_weights = {   # weight of attributes for value calculation
        "fish": 1,
        "junk": 0
    }
    # (attribute_weight) * (rarity_weight) * (area_id + 1)
    catchable_price = attribute_weights[attribute] * \
        rarity_weights[rarity] * (area + 1)
    if catchable_price == 0:
        continue
    else:
        # (catchable_id, buy_price)
        shop.append((c_id, catchable_price))


def catchable_gen(drop=False, stdout=False, toFile=False):
    # --------------------------------------------------
    # --- create drop table and create table queries ---
    # --------------------------------------------------
    dropQuery = "DROP TABLE IF EXISTS Catchable;"
    createQuery = """CREATE TABLE IF NOT EXISTS Catchable (
    catchable_id NUMBER PRIMARY_KEY UNIQUE,
    catchable_name TEXT NOT NULL,
    area_id NUMBER NOT NULL,
    xp_on_catch NUMBER NOT NULL,
    rarity TEXT NOT NULL,
    attribute TEXT NOT NULL);"""
    if drop:
        db.execute(dropQuery)
        db.execute(createQuery)
        # fill this table with as many tuples as needed for each item.
        db.executemany(
            "insert into Catchable values(?, ?, ?, ?, ?, ?);", catchable)
        db.commit()

    # -------------------------------------------------
    # --- properly formatted SQL command generation ---
    # -------------------------------------------------
    toOut = ""
    toOut += dropQuery + "\n"
    toOut += createQuery + "\n"
    toOut += "INSERT INTO Catchable\nVALUES\n"
    for i in range(0, catchable.__len__() - 1):
        tup = catchable.pop()
        toOut += "    ({0}, \"{1}\", {2}, {3}, \"{4}\", \"{5}\"),".format(*tup) + "\n"
    toOut += "    ({0}, \"{1}\", {2}, {3}, \"{4}\", \"{5}\");".format(*catchable.pop())
    if stdout:
        # to stdout
        print(toOut)
    if toFile:
        # to a file, either catchables.sql or catchables-TIMESTAMP.sql
        filename = "catchables.sql"
        if(os.path.exists("./sql/" + filename)):
            filename = timestamp + "-catchables" + ".sql"
        f = open(cwd + "/sql/" + filename, "w")
        f.write(toOut)


def areas_gen(drop=False, stdout=False, toFile=False):
    # --------------------------------------------------
    # --- create drop table and create table queries ---
    # --------------------------------------------------
    dropQuery = "DROP TABLE IF EXISTS Areas;"
    createQuery = """CREATE TABLE IF NOT EXISTS Areas (
    area_id NUMBER PRIMARY_KEY UNIQUE,
    area_name TEXT NOT NULL);"""
    if drop:
        db.execute(dropQuery)
        db.execute(createQuery)
        # fill this table with as many tuples as needed for each item.
        db.executemany("insert into Areas values(?, ?);", areas)
        db.commit()

    # -------------------------------------------------
    # --- properly formatted SQL command generation ---
    # -------------------------------------------------
    toOut = ""
    toOut += dropQuery + "\n"
    toOut += createQuery + "\n"
    toOut += "INSERT INTO Areas\nVALUES\n"
    for i in range(0, areas.__len__() - 1):
        tup = areas.pop()
        toOut += "    ({0}, \"{1}\"),".format(*tup) + "\n"
    toOut += "    ({0}, \"{1}\");".format(*areas.pop())
    if stdout:
        # to stdout
        print(toOut)
    if toFile:
        # to a file, either areas.sql or areas-TIMESTAMP.sql
        filename = "areas.sql"
        if(os.path.exists("./sql/" + filename)):
            filename = timestamp + "-areas" + ".sql"
        f = open(cwd + "/sql/" + filename, "w")
        f.write(toOut)


def items_gen(drop=False, stdout=False, toFile=False):
    # --------------------------------------------------
    # --- create drop table and create table queries ---
    # --------------------------------------------------
    dropQuery = "DROP TABLE IF EXISTS Items;"
    createQuery = """CREATE TABLE IF NOT EXISTS Items (
    item_id NUMBER PRIMARY_KEY UNIQUE,
    item_name TEXT NOT NULL,
    rarity TEXT NOT NULL,
    value NUMBER DEFAULT NULL,
    type TEXT NOT NULL,
    attribute TEXT DEFAULT NULL);"""
    if drop:
        db.execute(dropQuery)
        db.execute(createQuery)
        # fill this table with as many tuples as needed for each item.
        db.executemany("insert into Items values(?, ?, ?, ?, ?, ?);", items)
        db.commit()

    # -------------------------------------------------
    # --- properly formatted SQL command generation ---
    # -------------------------------------------------
    toOut = ""
    toOut += dropQuery + "\n"
    toOut += createQuery + "\n"
    toOut += "INSERT INTO Items\nVALUES\n"
    for i in range(0, items.__len__() - 1):
        tup = items.pop()
        toOut += "    ({0}, \"{1}\", \"{2}\", {3}, \"{4}\", \"{5}\"),".format(*tup) + "\n"
    toOut += "    ({0}, \"{1}\", \"{2}\", {3}, \"{4}\", \"{5}\");".format(*items.pop())
    if stdout:
        # to stdout
        print(toOut)
    if toFile:
        # to a file, either items.sql or items-TIMESTAMP.sql
        filename = "items.sql"
        if(os.path.exists("./sql/" + filename)):
            filename = timestamp + "-items" + ".sql"
        f = open(cwd + "/sql/" + filename, "w")
        f.write(toOut)


def inventory_gen(drop=False, stdout=False, toFile=False):
    # --------------------------------------------------
    # --- create drop table and create table queries ---
    # --------------------------------------------------
    dropQuery = "DROP TABLE IF EXISTS Inventory;"
    createQuery = """CREATE TABLE IF NOT EXISTS Inventory (
    user_id NUMBER NOT NULL,
    item_id NUMBER NOT NULL,
    amount NUMBER NOT NULL);"""
    if drop:
        db.execute(dropQuery)
        db.execute(createQuery)

    # -------------------------------------------------
    # --- properly formatted SQL command generation ---
    # -------------------------------------------------
    toOut = ""
    toOut += dropQuery + "\n"
    toOut += createQuery
    if stdout:
        # to stdout
        print(toOut)
    if toFile:
        # to a file, either inventory.sql or inventory-TIMESTAMP.sql
        filename = "inventory.sql"
        if(os.path.exists("./sql/" + filename)):
            filename = timestamp + "-inventory" + ".sql"
        f = open(cwd + "/sql/" + filename, "w")
        f.write(toOut)


def basket_gen(drop=False, stdout=False, toFile=False):
    # --------------------------------------------------
    # --- create drop table and create table queries ---
    # --------------------------------------------------
    dropQuery = "DROP TABLE IF EXISTS Basket;"
    createQuery = """CREATE TABLE IF NOT EXISTS Basket (
    user_id NUMBER NOT NULL,
    catchable_id NUMBER NOT NULL,
    amount NUMBER NOT NULL);"""
    if drop:
        db.execute(dropQuery)
        db.execute(createQuery)

    # -------------------------------------------------
    # --- properly formatted SQL command generation ---
    # -------------------------------------------------
    toOut = ""
    toOut += dropQuery + "\n"
    toOut += createQuery
    if stdout:
        # to stdout
        print(toOut)
    if toFile:
        # to a file, either basket.sql or basket-TIMESTAMP.sql
        filename = "basket.sql"
        if(os.path.exists("./sql/" + filename)):
            filename = timestamp + "-basket" + ".sql"
        f = open(cwd + "/sql/" + filename, "w")
        f.write(toOut)


def users_gen(drop=False, stdout=False, toFile=False):
    # --------------------------------------------------
    # --- create drop table and create table queries ---
    # --------------------------------------------------
    dropQuery = "DROP TABLE IF EXISTS Users;"
    createQuery = """CREATE TABLE IF NOT EXISTS Users (
    user_id NUMBER PRIMARY_KEY NOT NULL,
    xp NUMBER NOT NULL,
    gold NUMBER NOT NULL,
    current_area NUMBER NOT NULL,
    fish_caught NUMBER NOT NULL);"""
    if drop:
        db.execute(dropQuery)
        db.execute(createQuery)

    # -------------------------------------------------
    # --- properly formatted SQL command generation ---
    # -------------------------------------------------
    toOut = ""
    toOut += dropQuery + "\n"
    toOut += createQuery
    if stdout:
        # to stdout
        print(toOut)
    if toFile:
        # to a file, either users.sql or users-TIMESTAMP.sql
        filename = "users.sql"
        if(os.path.exists("./sql/" + filename)):
            filename = timestamp + "-users" + ".sql"
        f = open(cwd + "/sql/" + filename, "w")
        f.write(toOut)


def shop_gen(drop=False, stdout=False, toFile=False):
    # --------------------------------------------------
    # --- create drop table and create table queries ---
    # --------------------------------------------------
    dropQuery = "DROP TABLE IF EXISTS Shop;"
    createQuery = """CREATE TABLE IF NOT EXISTS Shop (
    catchable_id NUMBER NOT NULL,
    buy_price NUMBER NOT NULL);"""
    if drop:
        db.execute(dropQuery)
        db.execute(createQuery)
        # fill this table with as many tuples as needed for each item.
        db.executemany("insert into Shop values(?, ?);", shop)
        db.commit()

    # -------------------------------------------------
    # --- properly formatted SQL command generation ---
    # -------------------------------------------------
    toOut = ""
    toOut += dropQuery + "\n"
    toOut += createQuery + "\n"
    toOut += "INSERT INTO Shop\nVALUES\n"
    for i in range(0, shop.__len__() - 1):
        tup = shop.pop()
        toOut += "    ({0}, {1}),".format(*tup) + "\n"
    toOut += "    ({0}, {1});".format(*shop.pop())
    if stdout:
        # to stdout
        print(toOut)
    if toFile:
        # to a file, either shop.sql or shop-TIMESTAMP.sql
        filename = "shop.sql"
        if(os.path.exists("./sql/" + filename)):
            filename = timestamp + "-shop" + ".sql"
        f = open(cwd + "/sql/" + filename, "w")
        f.write(toOut)


def exec(drop, stdout, toFile, include_user_data_tables):
    # make sure the dir exists if you do toFile
    if toFile:
        try:
            os.mkdir(cwd + "/sql/")
        except:
            pass
    # databases that store data are under a check so I
    # don't accidentally overwrite any user data unless necessary
    if include_user_data_tables:
        inventory_gen(drop=drop, stdout=stdout, toFile=toFile)
        if not stdout:
            if drop:
                print("Reset inventory data.")
            else:
                print("Generated inventory file.")
        basket_gen(drop=drop, stdout=stdout, toFile=toFile)
        if not stdout:
            if drop:
                print("Reset basket data.")
            else:
                print("Generated basket file.")
        users_gen(drop=drop, stdout=stdout, toFile=toFile)
        if not stdout:
            if drop:
                print("Reset user data.")
            else:
                print("Generated user file.")

    # rest of the tables are fine to reset
    catchable_gen(drop=drop, stdout=stdout, toFile=toFile)
    if not stdout:
        if drop:
            print("Updated catchable data.")
        else:
            print("Generated catchable file.")
    areas_gen(drop=drop, stdout=stdout, toFile=toFile)
    if not stdout:
        if drop:
            print("Updated area data.")
        else:
            print("Generated area file.")
    items_gen(drop=drop, stdout=stdout, toFile=toFile)
    if not stdout:
        if drop:
            print("Updated item data.")
        else:
            print("Generated item file.")
    shop_gen(drop=drop, stdout=stdout, toFile=toFile)
    if not stdout:
        if drop:
            print("Updated shop data.")
        else:
            print("Generated shop file.")
    if not stdout:
        print("Done.")


db = sqlite3.connect(database_file_location)
# execute script.
# can call this from somewhere else if you really need, that's why i made it like this.
exec(drop, stdout, toFile, include_user_data_tables)
