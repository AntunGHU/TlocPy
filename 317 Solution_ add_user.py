import csv

def add_user(first_name, last_name):
    with open("users.csv", "a") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])
        
add_user("Colt", "Steele") # None
add_user("Grace", "Hopper") 
add_user("Hello", "World") # Users updated: 1.
add_user("Colt", "Steele") 
add_user("Boba", "Fett") # Users updated: 2.

