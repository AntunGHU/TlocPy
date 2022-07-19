# 7'39

# To move cursor - "seek" method; update story.txt sa 2 recenice pa
file = open("story.txt")
print(file.read())  # This short story is really short
# ____________________Now it is little longer
# ____________________The End
print(file.read())    #
print(file.seek(0))   # 0
print(file.read())  # This short story is really short
# ____________________Now it is little longer
# ____________________The End
print(file.read())    #
print(file.seek(1))   # 1
print(file.read())  # his short story is really short
# ____________________Now it is little longer
# ____________________The End
print(file.read())    #

# Dok read cita citav file, "readline" cita liniju
print(file.seek(0))   # 0
print(file.readline())  # This short story is really short
print(file.read())    # Now it is little longer
# ______________________The End
print(file.seek(0))   # 0
print(file.readline())  # This short story is really short
print(file.readline())  # Now it is little longer
print(file.readline())  # The End
print(file.readline())

# Method "readlines" izbacuuje sve linije kao elemente liste!
print(file.seek(0))   # 0
# ['This short story is really short\n', 'Now it is little longer\n', 'The End']
print(file.readlines())
print(file.read())  #

# File i promjene dok je otvoren te Closing a File
# ___Sto god unesemo u fajl i snimimo, automatski je Py-u na raspolaganju
# ___Vazno je da fajl zatvorimo kako nebi trosili resurse
# ___Zatvaramo w/ "close" method a provjera sa "closed" atributom
# ___Jednom zatvoren file vise se ne moze citati bez ponovnog otvaranja sa "open"

print(file.closed)  # False
print(file.close())  # None
print(file.closed)  # True
# print(file.read())  # Traceback(most recent call last):
# ____________________File "/home/antun/Documents/aCod/TlocPy/30_FileIO/306_ReadingFiles_Seek&Cursors.py", line 38, in <module >
# ____________________print(file.read())
# ____________________ValueError: I/O operation on closed file.

print(file.seek(0))  # Traceback(most recent call last):
# ____________________File "/home/antun/Documents/aCod/TlocPy/30_FileIO/306_ReadingFiles_Seek&Cursors.py", line 51, in <module >
# ____________________print(file.seek(0))
# ____________________ValueError: I/O operation on closed file.

# slides
# ? Closing a File
# ? You can close a file with the close method
# ? You can check if a file is closed with the closed attribute
# ? Once closed, a file can't be read again
# ? Always close files - it frees up system resources!
