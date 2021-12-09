# FISHERBOT - A Fun Fishing Bot for Discord
## Overview
Fisherbot is a Discord bot made to work like an incremental game. The idea is to catch fish and sell it. The fish can then be sold for gold and the gold can be used to purchase fishing rods. That's it.

There are 5 different areas:
 1. The Ocean
 2. Deep Cave
 3. Lava Pool
 4. Outer Space
 5. Dimensional Rift

Each area requires a different fishing rod to fish in.
The respective fishing rods are:
 1. Basic Rod
 2. Glow Rod
 3. Lava Rod
 4. Heavy Rod
 5. Omni Rod

Each area has different fish, and the better the area the better the fish. Each area also contains one new rarity of fish, increasing the value of every cast.

## Audience
The target audience of something like this is anyone. Anyone can add this bot to a server, type `f`, and fish their first fish. It's extremely simple and actually pretty fun if you need something simple to do.

## User Interface
A discord bot is essentially the same as a command-line interface (CLI) rather than your typical graphical user interface (GUI). The bot itself is a fairly simple front-end to the database and cannot really break anything since I used prepared statements in the database access functions file `dbf.py`. If anyone breaks something, it's me. This is because the users of this only have access to the database based on commands I create in the `bot.py` file. This means that I could actually create a GUI front-end for this if I intended to, since all the database access functions are done in a file separate to the bot running file. The actual logic for using the database access functions is the same regardless of the UI.

## DBMS
The RDBMS used in this is sqlite3. This makes the most sense for a project like this since it's self-contained to a file for extreme portability (I can send you a `.db` file and it's the actual usable in-production database with all inserted user and inventory data). Also, it's extremely lightweight and does not require any server setup and connection string nonsense like some other popular RDBMS (not pointing any fingers, MySQL). The access is done with a path to the `.db` file.

## Language
The programming language I chose to use is Python. I know and could have used Java, but frankly it's a mess and requires too much work to set up the environment. Python is faster for me to write and easier to include all the source in one folder. Since the focus is *mostly* the back-end, Python is overall a great choice.

Since everything is contained in its own folder, the only things actually required to make the bot function are
 1. sqlite3 for the system
 2. sqlite3 for python
 3. python 3.9.9 for the system
 4. nextcord for python

Four. Just 4 dependencies and two of them are the database language and the programming language.

## Timeline
Since I'm writing this fairly late, I'm almost finished with the front-end and back-end. Most work was done between `3-5 December` since I had a final on `7 December`.

### Completed
#### Beginning milestones
 * Basic database structure
   * Users
   * Inventory
   * Fish
   * Rods
   * Areas
 * Basic bot structure
   * Create bot user
   * Learn differences between new nextcord API and old discord.py
   * Copy bot template from API documentation and test with token
 * Bot function file
   * Basic getItemFromTable
   * Basic insertItemIntoTable
   * Random fish selection
   * Create user

#### Grind
 * Command functionality (PAIN AND SUFFERING)
   * `f`(ishing)
     * random fish selection
     * inventory insert algorithm
   * `shop` queries for selling fish
     * "dynamic" embed building
   * `area`
     * current area
     * area switching
   * `xp` checking
   * `sell`(ing) fish for gold
   * `inv`(entory) access
 * Database function "library"
   * Basically add all functions required to perform commands
   * Nothing in particular; keep it "minimal"
 * Database rework
   * Fish and Junk combined to Catchables
   * Rods into Items
   * Inventory split into Basket and Inventory
     * Catchable into Basket
     * Items into Inventory
   * Shop table created
 * ~~DB generation script for ease of use~~
   * Broken due to syntax change in database creation :(

### Future
 * `buy` shop
 * `rods` for explanation
 * `profile`
   * amount of gold
   * some cool statistics
     * rarest fish
     * amount of fish
     * "account" age
 * fish length in database
 * date caught in database
 * DB Generation script rewrite

### Notes
Might not ever be finished with this project. It's something I really want to carry further than this class, and I'm known for having unfinished projects. Hope you enjoy and can use it. If not, I'll submit a presentation video for you.