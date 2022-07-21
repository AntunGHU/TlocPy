# 10'29
# re-modul kokumentacija: https://docs.python.org/3/library/re.html
# todo kopirati odgovore u korespondne linije koda

# import regex module
import re

# define our phone number regex
pattern = re.compile(r'\d{3} \d{3}-\d{4}')

# search a string with our regex
res = pattern.search('Call me at 415 555-4242 or 310 234-999!')

pattern
type(pattern)
help(pattern)
res
res.group()

res = pattern.findall('Call me at 415 555-4242 or 310 234-999!')
res

# pattern se ne mora praviti posebno, nego ga u serach mozemo staviti kao 1. argument ali ispred ide "re." a na kraju (kako bi dobili rezultat) "group()".

res = re.search(r'\d{3} \d{3}-\d{4}',
                'Call me at 415 555-4242 or 310 234-999!').group()

# Osobina ovakvog pristupa je da bez posebnog re-objekta (pattern-a) svaki put se "compile" obavlja iznova tako da ako ga koristimo cesto, bolje ga je imati zasebno. Sve isto vazi i za "findall" metod
