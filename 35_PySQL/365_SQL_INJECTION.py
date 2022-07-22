# 8'58

# Video koji objasnjava kako sprijeciti iskoristavanje nekih losijih osobina quaery-a. Osnovni kod Ath donio u pratecem fajlu "365 password.py" koji sam kopirao.
# Ako se baza usera u SQL-u propituje na pogresan nacin (direktnim popunjavanjem SQL_quaery-a) umjesan user moze prevariti kod i uci bez passworda!!!

import sqlite3
conn = sqlite3.connect("users.db")

# query = "CREATE TABLE users (username TEXT, password TEXT)" # koristi se 1x za kreiranje tablice a potom komma!
u = input("please enter your username...")
p = input("please enter your password...")
c = conn.cursor()

# ? THE BAD WAY!
# query = f"SELECT * FROM users WHERE username='{u}' AND password = '{p}'"
# ako u gornji quaery (sa direktnim inosom 'u' i 'p') kad se pojavi input zahtjev upisemo '_OR_1=1-- user ce proci iako nije znao password. Zasto? Prvi znak ' sa istimtakvim okolo {p} cini " i zavrsava empty-string password; OR 1=1 zajedno sa kompletiranim 1. " tvori izraz " OR 1=1 sto znaci: user password je empty string " ili tj OR 1=1 (sto je tocno ukupno jer je u sredini OR). Za kraj jos -- komentiraju zadnji ' single string!!!

# THE MUCH SAFER WAY
query = f"SELECT * FROM users WHERE username=? AND password =?"
c.execute(query, (u, p))
# sada pokusaji trick-unosa  ne prolaze!! FAILED LOGIN

result = c.fetchone()
if(result):
    print("WELCOME BACK")
else:
    print("FAILED LOGIN")

conn.commit()
conn.close()
