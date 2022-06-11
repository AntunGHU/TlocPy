import sqlite3
connection = sqlite3.connect("my_friends.db")
c = connection.cursor()
# insert_query = "INSERT INTO friends VALUES ('Mary', 'Louis', 17)"
insert_query = '''INSERT INTO friends 
                    VALUES ('Mary', 'Louis', 17)''' # radi i L4
c.execute(insert_query)
connection.commit()
connection.close()