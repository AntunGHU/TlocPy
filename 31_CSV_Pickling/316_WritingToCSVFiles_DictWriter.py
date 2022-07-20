# 11'55

# ili pisanje u CSV koristenjem "dict"-a, malo kompliciranije
# "DictWriter" kreira writer-object za pisanje u CSV
# "fieldnames" -kwarg for DictWriter specifying headers
# "writeheader" -method to write header-row
# "writerow" -method to write row based on dictionary

from csv import DictWriter
from csv import DictWriter, DictReader

with open("cats13.csv", "w") as file:
    headers = ["Name", "Breed", "Age"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Name": "Garfild",
        "Breed": "Orange Tabby",
        "Age": 10
    })

with open("example316.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadovken"
    })

# izgleda vise pisanja ali dobar u situacijama u kojima su nam date u dict-u, a i vise je eksplicitan! i laksi je za razumjeti: sve prema sklonosti

# primjer DictReader-a i DictWriter-a zajedno i pretvaranje visine iz cm u inche!


def cm_to_inch(cm):
    return float(cm)*0.393701


with open("fighters2.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
    headers = ("Name", "Country", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for f in fighters:
        csv_writer.writerow({
            "Name": f["Name"],
            "Country": f["Country"],
            "Height": cm_to_inch(f["Height (in cm)"])
        })


# * Slides
# Writing CSV Files
# Using Dictionaries
# ? DictWriter - creates a writer object for writing using dictionaries
# ? fieldnames - kwarg for the DictWriter specifying headers
# ? writeheader - method on a writer to write header row
# ? writerow - method on a writer to write a row based on a dictionary
with open("example.csv", "w") as file:
    headers = ["Character", "Move"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })


# Dictionaries or Lists?
# ? Using lists often means less code
# ? Using dictionaries is often more explicit

# Recap za txt i csv files
# ? You can read and write text files using open and with
# ? Files are automatically closed after use when using with
# ? You can set the mode for open to read, write, or append
# ? The CSV module lets you read / write CSV files
# ? You can read / write CSVs using lists or dictionaries
