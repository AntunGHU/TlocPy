# 8'44

# Posto kod moze biti dosta dug a inace iza "=" idu "", mozemo koristiti triple """ sto nam omogucava da stavljamo kod u vise linija!!!

import sqlite3  # za sve varijante dole


connection = sqlite3.connect("my_friends.db")  # sad ne kreira nego otvara
c = connection.cursor()
# sad malo SQL-a
# insert_query = "INSERT INTO friends VALUES ('Mary', 'Louis', 17)"
insert_query = '''INSERT INTO friends 
                    VALUES ('Mary', 'Louis', 17)'''  # radi i L4
c.execute(insert_query)
connection.commit()
connection.close()
# pokrecemo kod i ako nema odgovora sve radi ispravno, sad u sqlite3 dio k-di da provjerimo
# ? >sqlite3 my_friends.db
# ? sqlite> select * from friends
# ? sqlite> ^D
# dakle, hardcoded insert u bazu radi! ali! za to nam nije trebao Py. Py dolazi kad imamo neku vrstu dinamickih podataka (CSV-fajl u SQL, email u SQL s varijablama)

# VARIJABLA WAY! Dodavanje "varijable" je moguce preko f""-formata ala
form_first = "Dana"
quaery = f"INSERT INTO friends (first_name) VALUES ('{form_first}')"
c.execute(quaery)
connection.commit()
connection.close()
# ali, zbog svih tih silnih zagrada to nije privlacna opcija!

# Bolja opcija (BETTER WAY!) je da umjesto ('{form_first}') ide samo (?) a samo znacenje upitnika prosljedjuje "tuple-arg" u sljedecoj "c.execute" liniji koda
form_first = "Dana"
quaery = f"INSERT INTO friends (first_name) VALUES (?)"
c.execute(quaery, (form_first,))  # !!! PAZNJA _ TUPLE-ARG!!!
connection.commit()
connection.close()
# A poslije sqlite> dio provjera

# NAJBOLJI WAY!!! Varijabla npr "data" unutar koje su svi djelovi potrebni za SQL-tablicu (ime, prezime, age)
data = ("Steve", "Irwin", 9)
quaery = "INSERT INTO friends VALUES (?,?,?)"
c.execute(quaery, data)
connection.commit()
connection.close()
# ? >sqlite3 my_friends.db
# ? sqlite> select * from friends # Steve|Irwin|9
# ? sqlite> ^D
