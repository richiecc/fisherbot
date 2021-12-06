# FISHERBOT

If you want to use this bot, head over to this [Discord server I made for it](https://discord.gg/CkbHNMkuym). It's only me and the bot there at the moment. I think you can join with a guest account in your browser (no account creation required) so give it a shot. I'll try to leave the bot running for as long as I can.

Below are for understanding how the python scripts work. You're probably more interested in how the database is created... Click the file `DATABASE.md` for that. Oh, also, `PROPOSAL.md` since I need a grade for that, I think.

## Requirements
### Generation of SQLite3 `.db` file and `.sql` scripts 
* [Python 3.9.9](https://www.python.org/downloads/release/python-399/)
* [sqlite3 for your OS](https://sqlite.org/index.html)
* [sqlite3 for python](https://docs.python.org/3/library/sqlite3.html)

### Starting your own Discord bot with the bot script
* [nextcord for python](https://pypi.org/project/nextcord/)
* General Discord bot knowledge
  * Create bot user
  * Get bot user token
  * Add bot user to server

## Using the bot in a server
 * `f` to fish
 * `inv` to access your inventory
 * `shop` for the shop help menu
   * `shop <rarity>` to view sell prices of fish for a rarity
 * `sell <amount> <fish>` to sell fish
   * `sell 1 Salmon` <--- CASE SENSITIVE FISH NAME!
 * `rods`
   * not implemented
 * `buy rod <rod>`
   * not implemented
 * `area` to see your current area
   * `area <num>` to set your area


## Generating SQL scripts and database with `gen_sql.py`
So, there's a script called `gen_sql.py` in this repo. If you want the SQL DROP/CREATE for the database, run it. Oh, before you run it...
### Configuration
Look for the section *configurables* near the top of the script
#### drop
 * Set **True** if you want changes to be committed to the `fisherbot.db` file
 * Set **False** if you do not want any changes to be committed to `fisherbot.db`

#### stdout
 * set **True** if you want the SQL script to be output to stdout
   * this is useful if you want to pipe the script into something, or write it to a single file directly from the command line
 * set **False** to keep the normal verbose/debug outputs

#### toFile
 * set **True** if you want individual SQL scripts for each table to output to `./sql/`
 * set **False** if you do not want scripts to be output

#### include_user_data_tables
 * set **True** to include *USER DATA CONTAINING TABLES* in the script
 * set **False** to avoid *USER DATA CONTAINING TABLES* in the script

## Understanding `dbf.py`
`dbf.py` contains all of the database interation functions used in `bot.py`. You can write your own program using these functions and basically piggyback on this database if you'd like. Keep in mind nothing is completely finished on the front-end side. <br> Basically: 
* Read the SQL statements in db.execute() function calls
* Look at the database diagram
* ??????
* Profit

## `bot.py`
Run this to run the bot. It's as simple as that. I haven't properly formatted this file for a true discord bot developing experience, but it's functional. Realistically I should be using actual bot commands instead of looking for a certain string for every message a user sends. Oh well.

## TODO
 * Profile
   * Profile picture
   * Total XP
   * Level
   * Number of fish caught
   * Gold
   * Rarest fish in basket
     * Date caught (needs db changes)
   * Rods/Areas Unlocked
 * Shop
   * Buy rods