import sqlite3
connection = sqlite3.connect("my_friends.db")
c = connection.cursor()
people = [("Anja1", "Glavan", 31),
          ("Anja2", "Glavan", 61),
          ("Anja3", "Glavan", 55)]
insert_query = "INSERT INTO friends VALUES (?, ?, ?)" #BEST
c.executemany(insert_query, people)
connection.commit()
connection.close()