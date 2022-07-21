# 9'18

# Prije koristenja RE-a za substitution pametno je prvo imati na umu mogucnosti string-metoda kao npr "replace"

import re

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

patern = re.compile(r'(Mr\.|Mrs\.|Ms\.) [a-z]+', re.I)

print(patern.findall(text))  # ['Mrs.', 'Mr.', 'Ms.']
print(patern.search(text).group())  # Mrs. Daisy
print(patern.search(text).groups())  # ('Mrs.',)

result = patern.sub("REDACTED", text)
print(result)   # Last night REDACTED and REDACTED murdered REDACTED

# ali ako hocemo da umjesto REDACTED bude npr "Mrs. D" itd, moramo koristiti oznake grupe iz regex-a uz sub-argument! Prvo bez D; W; C

# Ako ne pazimo na order onda obrne "REDACTED \g<1>"
result = patern.sub("\g<1> REDACTED", text)
print(result)  # Last night Mrs. REDACTED and Mr. REDACTED murdered Ms. REDACTED

# Ako zelimo i pocetno slovo imena onda ono mora postati "g<2>" a to radimo preuredjujuci i patern i result i nestavljajuci REDACTED ako ga ne zelimo

patern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result = patern.sub("\g<1> \g<2>", text)
print(result)  # Last night Mrs. D and Mr. W murdered Ms. C
