# 13'28

# ? WHAT ARE REGULAR EXPRESSIONS? A way of describing patterns within search strings
# RE nije samo Py-topic (kao ni npr http-requests)
# RE is a way to describe patterns in searchstring
# npr: procjena email-a "colt@gmail.com" Py-kodom bilo bi puno posla

# ? VALIDATING EMAILS
# colt@gmail.com    carly.simon@yahoo.com   rosa-98@meals.org   david+lee+roth@hotmail.com  shoe_queen91@hello.net
# Starts with 1 or more letter,number,+,_,-,. then      ** A single @ sign then      ** 1 or more letter, number, or -  then      ** A single dot then      ** ends with 1 or more letter, number,-, or .
# ? Let's use a regular expression!
# * (^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)

# ? POTENTIAL USE CASES
# Credit Card number validating #Phone number validating #Advanced find/replace in text #Formatting text/output

# ? FIRST,LET'S START WITH REGEX OUTSIDE OF PYTHON
# da bi RE koristili u Py-u koristimo RE-modul koji je ala adapter ili prilagodnik
