# 7'21

# Osim "r" i "w" imamo i
# "a" -otvara za pisanje ali dodaje na kraj, uvjek samo na kraj
# "r+"-otvara za pisanje na mjesto lokacije cursor-a
# "x" -otvara za pisanje ali samo ako istoimeni fajl jos ne postoji
# "t" -text mode
# "b" -binary mode
# "+" -otvara disk za update

# Modes for Opening Files
# ? r - Read a file (no writing) - this is the default
# ? w - Write to a file (previous contents removed)
# ? a - Append to a file (previous contents not removed)
# ? r+ - Read and write to a file (writing based on cursor)

# Truncating Files
# ? file.truncate - removes all text starting from the current cursor position

with open("haiku.txt", "r+") as file:
    file.write("ADDED USING r+")

file = open("haiku.txt")
print(file.read())  # ADDED USING r+is great
# ____________________Here's another line of text
# ____________________Closing now, goodbye!

# CURSOR BIO NA POCETKU PA JE STARI TEX PREPISAN!!!

print(file.close())  # None
print(file.closed)  # True

# sad malo sa seek-anjem

with open("haiku.txt", "r+") as file:
    file.write("-:)")
    file.seek(10)
    file.write("-:(")

file = open("haiku.txt")
print(file.read())  # -:)ED USIN-:(+is great
# ___________________Here's another line of text
# ___________________Closing now, goodbye!

print(file.close())  # None
print(file.closed)  # True

# ako pokusamo "r+" sa nepostojecim fajlom za razliku od "w" ili "a" koji kreiraju fajl, "r+" ce vratiti gresku

# FileNotFoundError: [Errno 2] No such file or directory: 'nepostojeci.txt'
with open("nepostojeci.txt", "r+") as file:
    file.write("-:)")
    file.seek(10)
    file.write("-:(")
