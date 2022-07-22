# 7'19

# Zbog npr. potreba WebSeit-ova kad trebamo komunicirati s DB (npr neko submit-a neki obrazac, obrazac trigera Py u backend-u koji BB...)
# Py dolazi s builtin library za SQLite (razlog biranja SQLite-a) "sqlite3". Dokumentacija o "sqlite3" u PyDoc-u https://www.sqlite.org/index.html i https://docs.python.org/3/library/sqlite3.html
# Da bi mogli use-ati sqlite3: 1.kreiramo Connection-object u kome se stora date. Ath kreira "Friends"-dir i u njemu "friends.py". Pokraj je fajl "basics.sql"

import sqlite3
conn = sqlite3.connect("my_friends.db")  # pravi "connection" i novu db!
# linije koda potrebne za kreiranje kursora, creiranje tabela s sql-kdama te komitanje promjena prema db-eu

c = conn.cursor()  # create cursor
c.execute("CREATE TABLE friends (ime TEXT, prezime TEXT, age INTEGER);")
conn.commit()

# Iza bilo kakvih unosa sve mora zavrsiti sa
conn.close()

# pregled u termu sa "ls" pokazuje fajlove "my_friends.db"  i "friends.py" a sljedece pokretanje istih k-di nece ponovo praviti "my_friends.db" nego ce se samo s njom povezati.

# Sljedi kreiranje tabela linijama koda koje se smjestaju izmedju "conn" i "conn.close()"

# nakon svega i odrade ovog koda kojeg ath donosi i u posebnom fajlu "friends.py" ath ide u term i komandama
# ? sqlite3 my_friends.db
# ? sqlite> .tables  #
# ? sqlite> .shema friends #
# provgjerava kako su odradjene prethodne sekvence. Vidi fajl friends.py kojeg prvo pokrecem untar ove Sekcije pa ako ne odradi onda cu iz root-a projekta
# dakle, pokrecuci fajl iz mape 35 my_friends.db stvorio se unutar root-a tj na mjestu na kom se nalazi projekt! Isto bi bilo i da sam fajl "friend.py" iz root-a pokrenuo. Polozaj py-fajla koji nesto odradjuje nema nikakve veze. On ce samo djelovati na izvrsnu k-u da bude prilagodjena tome ali ce kreiranja raditi tamo gdje je def. a to je mjesto gdje se nalazimo tj root-projekta!! ZAPAMTIMO OVO!!!
# ? antun@ub:~/Documents/aCod/TlocPy$ /bin/python3 /home/antun/Documents/aCod/TlocPy/35_PySQL/friends.py
# term-dio kdi potvrdjuje da je sve ok odradilo!!
