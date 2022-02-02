import sqlite3

"""
Recreates database.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@ WILL DELETE ALL DATA @@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
ONLY USE TO COMPLETELY REGENERATE DATABASE.
"""
# https://stackoverflow.com/questions/54289555/how-do-i-execute-an-sqlite-script-from-within-python
with open('database.sql', 'r') as sql_file:
    script = sql_file.read()


db = sqlite3.connect('fisherbot.db')
cursor = db.cursor()
cursor.executescript(script)
db.commit()
print("Done.")
db.close()
