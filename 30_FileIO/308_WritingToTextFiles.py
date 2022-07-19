# 3'55

# Writing Files
# ? You can also use open to write to a file
# ? Need to specify the "w" flag as the second argument

with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")


# IMPORTANT: If you open the file again to write, the original contents will be deleted!

file = open("haiku.txt")
print(file.read())  # Writing files is great
# ____________________Here's another line of text
# ____________________Closing now, goodbye!
print(file.close())  # None
print(file.closed)  # True


# alternativa bez "with"

file = open("antun.txt", "w")
file.write("impro pjesme pjesnika antuna")
print(file.close())

file = open("antun.txt")
print(file.read())
print(file.close())

# pokusaj dodavanja u fajl "haiku.txt" sa "w"-modom rezultira potpunim brisanjem starog teksta i pisanjem novog!  Modovi!!!
