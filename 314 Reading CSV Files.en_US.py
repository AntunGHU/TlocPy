from csv import reader
with open ("fighters.csv") as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)
                
with open ("fighters.csv") as file:
    csv_reader = reader(file)
    next(csv_reader)        
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
        
with open ("fighters.csv") as file:
    csv_reader = reader(file)
    data = list(csv_reader)        
    print(data)
    
from csv import DictReader
with open ("fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row)
        
from csv import DictReader
with open ("fighters2.csv") as file:
    csv_reader = DictReader(file, delimiter = "$")
    for row in csv_reader:
        print(row)
        
with open ("fighters2.csv") as file:
    csv_reader = reader(file, delimiter="$")
    next(csv_reader)        
    for fighter in csv_reader:
        print(f"{fighter[0]} is from {fighter[1]}")
        