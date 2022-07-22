# 6'59

# ? sqlite> SELECT name FROM dogs;      # Champ; Rose; Mose
# ? sqlite> SELECT name, age FROM dogs; # Champ|4; Rose|11; Mose|5
# prije pokaza kako selektirati druge informacije , jos dodaje 4 unosa preko ".read basics.sql".
# ? sqlite>.read basic.sql
# ? sqlite> SELECT * FROM dogs; # daje sve unose i sve kolone
# ? sqlite> SELECT * FROM dogs WHERE name IS "Piggy";
# ? sqlite> SELECT * FROM dogs WHERE breed IS "Husky";
# ? sqlite> SELECT name FROM dogs WHERE breed IS "Husky";
# ? sqlite> SELECT * FROM dogs WHERE breed IS NOT "Chiuaia";
# ? sqlite> SELECT * FROM dogs WHERE age > 9;
# ? sqlite> SELECT * FROM dogs WHERE name LIKE "%gg";
# ? sqlite> SELECT name FROM dogs WHERE
# Fast and furious through SQL ali dovoljno za Py u vezi s SQL!!!
