# 5'01

# ? sqlite> .table
# ? sqlite> INSERT INTO cats (name, breed, age) VALUES("blue", "Foli", 3);
# ? sqlite> SELECT * FROM CATS;   # blue|Foli|3

# Sve gore je pisano u sqlite> promptu. Ali moze se prvo sve komande staviti u *.sql fajl. Pravi "basic.sql" i editira ga sa 4 slicna unosa te potiva poslije taj fajl na sljedeci nacin:
# ? sqlite3 cat_db.db
# ? > .tables   # cats
# ? > .read basic.sql #trebalo bi da ga procita i sve izvrsi ali to ne ide lako u Win-sima
# ? > .tables   # cats
# ? sqlite> SELECT * FROM CATS;  # i trabalo bi da se vide novi unosi!
