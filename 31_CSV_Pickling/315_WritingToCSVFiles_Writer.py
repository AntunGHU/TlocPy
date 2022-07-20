# 9'07

# ili pisanje u CSV koristenjem "list"a.
# "writer" kreira writer-object za pisanje u CSV
# "writerow" - metod za pisanje row ili reda u CSV

from csv import writer, reader

with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryn", "Hodocken"])

# Ath malo mjenja primjer u:

with open("cats.csv", "w") as file:  # Stvara se cats.csv
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["Kitty", 1])

# Dalje Ath zeli stvoriti scream.py sa kojim ce kapitalizirati "fighters.csv"
with open("fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]
with open("screaming_fighters.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

# Ath daje i rijesenje sa gnjezdenjem koda ciji je nedostatak: ne zatvara fajl figters.csv
with open("fighters.csv") as file:
    csv_reader = reader(file)
    with open("screaming_fighters.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])


# * Slides
# Writing CSV Files
# Using Lists
# ? writer - creates a writer object for writing to CSV
# ? writerow - method on a writer to write a row to the CSV
from csv import writer
with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])
