# 13'08

# CSV podaci su tabularni i cesto se pojavljuju. Mozemo ih citati kao i txt-fajlove ali Py ima i built-in CSV-modul

# CSV Module:
# ___________# reader: lets you iterate over rows of the CSV as lists
# ___________# DictReader: let us iterate over rowe of the CSV as Ordered Dists with keys=headers

# *****reader*****
from csv import reader
with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)                # nacin da se preskoci header-row
    for row in csv_reader:
        print(row)                  # ['Ryu', 'Japan', '175']
# ....................................['Ken', 'USA', '175'] itd

with open("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
# ....................................Ryu is from Japan
# ....................................Ken is from USA

# ako zelimo csv pretvoriti u listu tj listu lista (slozenu listu)
with open("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)
    # [['Name', 'Country', 'Height (in cm)'], ['Ryu', 'Japan', '175'], ['Ken', 'USA', '175'], ['Chun-Li', 'China', '165'], ['Guile', 'USA', '182'], ['E. Honda', 'Japan', '185'], ['Dhalsim', 'India', '176'], ['Blanka', 'Brazil', '192'], ['Zangief', 'Russia', '214']]
    print(data)

# *****DictReader*****
from csv import DictReader
with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row)

from csv import DictReader
with open("fighters2.csv") as file:
    csv_reader = DictReader(file, delimiter="$")
    for row in csv_reader:
        # {'Name': 'Ryu', 'Country': 'Japan', 'Height (in cm)': '175'}
        # {'Name': 'Ken', 'Country': 'USA', 'Height (in cm)': '175'} itd
        print(row)
        print(row["Name"])  # Ryu2, Ken, Chun-Li itd

# other delimiters: reader accepts a delimiter kwarg in case your data has not ","
with open("fighters2.csv") as file:
    csv_reader = reader(file, delimiter="$")
    next(csv_reader)
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
