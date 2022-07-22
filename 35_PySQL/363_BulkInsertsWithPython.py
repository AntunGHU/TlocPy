# 4'55

import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()

people = [
    ("Roald", "Amundsen", 5),
    ("Rosa", "Parks", 8),
    ("Henry", "Hudson", 7),
    ("Neil", "Armstrong", 7),
    ("Daniel", "Boone", 3)]

quaery = "INSERT INTO friends VALUES (?,?,?)"

# Vise nacina upisa liste-tuplova "people"

# 1) nacin
# c.executemany(quaery, people)
# i nakon odrade fajla pokazuje se uspjesnost. Medjutim! Ovaj nacin nije dobar ako pored upisa u db trebamo i nesto obaviti.

# Tada koristimo 2).-loop nacin.
average = 0
for person in people:
    # c.execute("INSERT INTO friends VALUES (?,?,?)", person) #ili
    c.execute(quaery, person)
    average += person[2]
print(average/len(people))

# commit changes
conn.commit()
conn.close()
