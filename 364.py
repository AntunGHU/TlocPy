import sqlite3
connection = sqlite3.connect("my_friends.db")
c = connection.cursor()
#0 c.execute("SELECT * FROM friends")
#1 print(c)                                 <sqlite3.Cursor object at 0x7f0d423f0d40>
#2 for result in c:
#2    print(result)                         ('Mary', 'Louis', 17)
#2                                          ('Dana1', None, None)
#2                                          ('Dana2', None, None)
#2                                          ('Anja', 'Glavan', 31)
#2                                          ('Anja1', 'Glavan', 31)
#2                                          ('Anja2', 'Glavan', 61)
#2                                          ('Anja3', 'Glavan', 55)
#2                                          ('Anja1', 'Glavan', 31)
#2                                          ('Anja2', 'Glavan', 61)
#2                                          ('Anja3', 'Glavan', 55)
#3 print(c.fetchall())                      [('Mary', 'Louis', 17), ('Dana1', None, None),         ('Dana2', None, None), ('Anja', 'Glavan', 31), ('Anja1', 'Glavan', 31), ('Anja2', 'Glavan', 61), ('Anja3', 'Glavan', 55), ('Anja1', 'Glavan', 31), ('Anja2', 'Glavan', 61), ('Anja3', 'Glavan', 55)]
c.execute("SELECT * FROM friends WHERE ime IS 'Mary'")
print(c.fetchone())                      # ('Mary', 'Louis', 17)
connection.commit()                     
connection.close()                      