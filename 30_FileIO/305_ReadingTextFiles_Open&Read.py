# 6'03

# we can open and read file with "open" fn
# "open" returns a file-object ili OSError
# we can read with "read" fn
# documentacion pod "https://docs.python.org/"
# open(file,mode='r', buffering...)

# File Read Example:
file = open("story.txt")
print(file)  # < _io.TextIOWrapper name = 'story.txt' mode = 'r' encoding = 'UTF-8' >
print(file.read())  # This short story is really short
print(file.read())  # (prazno! :-( nema vise! Coursor Movement!)

# Cursor Movement:
# Py reads by cursor, ala typing by cursor
# poslije prvog citanja cursor je na kraju


# slides: ReadingFiles
# ? You can read a file with the open function
# ? open returns a file object to you
# ? You can read a file object with the read method
# slides: CursorMovement
# ? Python reads files by using a cursor
# ? This is like the cursor you see when you're typing
# ? After a file is read, the cursor is at the end
# ? To move the cursor, use the seek method
# ? To read only part of a file, pass a number of characters into read, or use readline
# ? To get a list of all lines, use readlines
