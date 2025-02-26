# FISHERBOT
A weird school project 

## Requirements
### Generation of SQLite3 `.db` file and `.sql` scripts 
* [Latest python](https://www.python.org/downloads/)
* (Recommended) [sqlite for your OS](https://sqlite.org/index.html)

### Starting your own Discord bot with the bot script
* [discord.py for python](https://pypi.org/project/discord.py/)
* General Discord bot knowledge
  * Create bot user
  * Get bot user token
  * Add bot user to server
  * Add message content intent
  * etc.
* Create `bot_token.py` with the following content:

      token = "YOUR_TOKEN_HERE"

## Bot Commands aka HELP
 * `f` to fish
 * `inv` to access your inventory
 * `bal` or `balance` to view current gold balance
 * `shop` for the shop help menu
   * `shop <rarity>` to view sell prices of fish for a rarity
 * `sell` to sell items
   * `sell <amount> <fish>`
   * `sell 1 Salmon` <--- CASE SENSITIVE FISH NAME!
   * `sell fish` to sell all fish
   * `sell junk` to sell all junk
   * `sell all` to sell both fish and junk
 * `xp` to check total xp
 * `rods` to viewrods all purchasable rods
 * `buy rod <rod name>` to buy the rod (use name given by `rods`) 
 * `area` to see your current area
   * `area <num>` to set your area
 * `profile` to show off your profile
   * `profile @user` to see someone else's profile

## Understanding `dbf.py`
`dbf.py` contains all of the database interation functions used in `bot.py`. You can write your own program using these functions and basically piggyback on this database if you'd like. Keep in mind nothing is completely finished on the front-end side. <br> Basically: 
* Read the SQL statements in db.execute() function calls
1. Look at the database diagram
2. ??????
3. Don't understand because it's outdated

## `bot.py`
Run this to run the bot. It's as simple as that. I haven't properly formatted this file for a true discord bot developing experience, but it's functional. Realistically I should be using actual bot commands instead of looking for a certain string for every message a user sends. Oh well.

## TODO
 * SQL script generator
 * fix terrible string replace

<del>

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

</del>
