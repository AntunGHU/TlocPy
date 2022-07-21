# 8'45

import re
# Imamo sljedece flagove: A(ASCII), S(DOTALL), I(IGNORECASE), L(LOCALE), M(MULTILINE), X(VERBOSE)
# X omogucava bolju organizaciju RE izraza pa tako jedan tipican ali i ne i pretjerano dugacak RE

# pat = re.compile(r'^([a-z0-9_\.-]+)@([a-z0-9_\.-]+)\.([a-z\.]{2,6})$')

# koristeci flag X mozemo reorganizirati na vise linija!! jer s njimse ignorira whitespace ali ako ga bas trebamo mozemo ga ubaciti sa "\ "

pat = re.compile(r"""
        ^([a-z0-9_\.-]+) # prvi dio
        @                # @ sign
        ([a-z0-9_\.-]+)  # email name
        \.               # tocka
        ([a-z\.]{2,6})$
        """, re.X)

match = pat.search("thomas123@yahoo.com")
print(match.group())    # thomas123@yahoo.com
print(match.groups())   # ('thomas123', 'yahoo', 'com')

# pokusaj brisanja re.X doveo do greske!!! "AttributeError: 'NoneType' object has no attribute 'group'"

# ako uz flag X zelimo dodati jos neki npr I dodajemo ga sa "|" tako da to izgleda "re.X|re.I". Imajuci "re.I" u RE vise ne moramo pisati [A-Za-z] nego je dovoljno samo [a-z]
