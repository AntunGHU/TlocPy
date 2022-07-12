# 5'34

# Iterator: ako next() vraca element, npr next("HELLO") --> "H", next("HELLO") --> "E" itd
# Iterable: ako ga iter() moze pretvoriti u iteratora
# >>> name = "Oprah"
# >>> it = iter(name)
# >>> next(it)	# 'O'
# >>> next(it)	# 'p'		itd ili 
# >>> nums = [1,2,3]
# >>> it = iter(nums)
# >>> next(it)	# 1
# >>> next(it)	# 2
# >>> next(it)	# 3
# >>> next(it)	# StopIteration

#! PROBLEME UZROKOVAO PREIMENOVANJEM MAPE py U $py!!!
# In Python, when you reference a file, it needs to exist. Otherwise, Python will return a FileNotFoundError: [Errno 2] No such file or directory.
# In this tutorial, let’s look at what is #? FileNotFoundError: [Errno 2] No such file or directory error means and how to solve this in your code.

#todo ***Python FileNotFoundError: [Errno 2] No such file or directory
# Python will raise FileNotFoundError when you use the OS library and try to read a file or write a file that does not exist using an open() statement.
# It is, of course, excluding you are creating a new file and writing content to the file. Any error message which states FileNotFoundError means that Python cannot find the path of the file you are referencing.
#todo ***Example FileNotFoundError
# The below code will list all the files in a specified folder. We will be using the OS module and os.listdir() method to get a list of files in the specified folder.
#? import os
#? for f in os.listdir("/etc"):
#? 	    print(f)

# *Output
#? Traceback (most recent call last):
#?   File "Main.py", line 2, in <module>
#?     for f in os.listdir("/etc/test"):
#? FileNotFoundError: [Errno 2] No such file or directory: '/etc/test'
# Now you can see that Python is throwing FileNotFoundError: [Errno 2] No such file or directory since the folder reference is wrong here.
#The possible reasons for this error could be as follows.

#todo ***Misspelled file name
# The error will often occur due to misspelled filenames, so providing the correct file name would solve the issue.

#todo ***Invalid file path or directory path
# Sometimes you might give a wrong file path or directory path which does not exist. It usually happens even with the network path when it’s unreachable. So ensure that the file path is correct and if you are placing the file in the network path, make sure it’s reachable and accessible.

#todo ***Using a relative path
# If you use a relative path, the file would be searched in the current working directory and not in the original path. So ensure you give an absolute path of the file to resolve the error.

#todo ***Solution to FileNotFoundError: [Errno 2] No such file or directory
# We will correct our above code by referencing the proper directory where the file exists. This time, we will also use an absolute path instead of a relative path to ensure it’s referencing the correct directory.

import os
for f in os.listdir("C:/Projects/Tryouts/etc"): # "d:/za_PC/$py/aCode/TlocPy/27_IteratorsGenerators"
	print(f)

#* Output

#? python.txt
#? index.md
#? Python Data Science Ebook.pdf

