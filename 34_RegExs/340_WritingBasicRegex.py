# 10'09

# Tona RE simbola! "Satckoverflow" mjesto na kojem i Ath trazi kad zapne
# Vjezbanje na stranici: "https://pythex.org/" iako i njih ima tona
# "." bez iceka oznacava sve
# ")" bez kontre dovodi do greske "Invalid RE: unbalanced paretheses"
# RE CheetSheet: "http://www.rexegg.com/regex-quickstart.html"

# ostali zancajniji simboli:
# ? SOME REGEX SYNTAX:
\d digit 0-9
\w letter, digit, or underscore
\s whitespace character
\D not a digit
\W not a word character
\S not a whitespace character
.	any character except line break

# \d    i 3 i 23
# \d\d  samo 23 ali ne i 2_3 za to treba \d \d
# \w    sve rijeci, sve brojeve ali ne i @ : )
# \s    samo whitespace
# \w\s\w    "I like cats" oznaci "I l" i "e c"
# \D    sve sto nije broj: slova, whitespace, spec-znake(.,@:;)
# \W    prazno izmedju rjeci, tocke i : ) @
# \S    sve sto nije whitespace
# \w\w\w\w\w    rjeci s 5 slova; \s\w\w\w\w\w\s rjeci s 5 slova i space ispred,iza
