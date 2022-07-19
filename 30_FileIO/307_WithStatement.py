# 3'43

# "with" je drugi nacin otvaranja file-a koji ga automatski i zatvara (ne moramo posebno!)
with open("story.txt") as file:
    file.read()

file.closed  # True

# ili

with open("story.txt") as file:
    data = file.read()

print(data)  # This short story is really short
# _____________Now it is little longer
# _____________The End
print(file.closed)  # True
print(file.read())  # Traceback (most recent call last):
# ____________________File "/home/antun/Documents/aCod/TlocPy/30_FileIO/307_WithStatement.py", line 9, in <module>
# ____________________print(file.read())
# ____________________ValueError: I/O operation on closed file.

# Ath malo o __enter__() i __exit__() dunder-metodima. Oni su ala interface of with-statement koje mozemo i sami modati

# Ovu sintaksu sa "with" koristi vecina jer ne moramo brinuti o zatvaranju, malo je kraca procedura da sve procitamo i obe operacije (open i read) su odmah pozvane a ne pojedinacno!
