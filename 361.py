import sqlite3
connection = sqlite3.connect("my_friends.db")
c = connection.cursor()
c.execute("CREATE TABLE friends (ime TEXT, prezime TEXT, starost INTEGER)")
connection.commit()
connection.close()