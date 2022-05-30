import sqlite3
connection = sqlite3.connect("my_friends.db")
c = connection.cursor()
form_data = ("Anja", "Glavan", 31)
# insert_query = f"INSERT INTO friends (ime) VALUES ('{form_first}')" #BAD
# insert_query = f"INSERT INTO friends (ime) VALUES (?)" #BETTER
insert_query = "INSERT INTO friends VALUES (?, ?, ?)" #BEST
c.execute(insert_query, form_data)
connection.commit()
connection.close()