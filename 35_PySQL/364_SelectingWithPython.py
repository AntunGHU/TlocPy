# 44'36

# sadrzaj uglavnom kao i prateci fajl "364 selecr.py" uz par komentara

import sqlite3
conn = sqlite3.connect("my_friends.db")
# create cursor object
c = conn.cursor()
# print(c) # <sqlite3.Cursor object at 0x7f0674711b90> # nije iterator
# c.execute("SELECT * FROM friends WHERE first_name IS 'Rosa'")
c.execute("SELECT * FROM friends WHERE closeness > 5 ORDER BY closeness")


# Iterate over cursor
# for result in c:
#     # ('Steve', 'Irwin', 9) # izbacuje sve zapise kao tuplove pojedinacne
#     print(result)

# Fetch One Result
# print(c.fetchone())   # izbacuje samo jedan rezultat-tupl

# Fetch all results as list
print(c.fetchall())  # [('Steve', 'Irwin', 9)] rezultati kao lista tuplova
# zgodno ako zelimomkao bulk insertirati u neku drugu tabelu!!


# commit changes
conn.commit()
conn.close()

# cesto radi printove kao najbrzi uvid u djelovanje k-de!
