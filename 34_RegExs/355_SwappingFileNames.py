# 9'02

import re
titles = [
    "Significant Others (1987)",
    "Tales of the City (1978)",
    "The Days of Anna Madrigal (2014)"
]
titles.sort()   # in place pa ..
# i ide po abacednom redu sto nije uvijek ono sto zelimo. Recimo da zelimo da prva bude godina izdanja pa naslov.
# ['Significant Others (1987)', 'Tales of the City (1978)', 'The Days of Anna Madrigal (2014)']
print(titles)

# prvo definiranje paterna za trazenje

# pattern = re.compile(r'(^[\w ]+) (\(\d{4}\))')
pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
# umjetno smo dodali whitespace izmedju 1. i 2. grupe (iako bi ga mogao oznaciti i sam [\w ]) zato sto bez toga "cvrstog" whitespace-a bi smo ostali bez njega jer bi ga naslov odnio na kraj a godina bi bez njega bila odmah uz naslov!
# Ath upozorava na problem 2.grupe (godina) koja ce bez dodatnih radnji i dalje imati zagrade!!!

result = pattern.sub("\g<2> - \g<1>", titles[0])
# print(result)  # (1987) - Significant Others

# sad kako bi izbacio zagrade doradjuje regex tako da () od g2 suzava kako bi ista bila samo oko brojki tj "(\d{4})" tako da sad g2 izgleda \((\d{4})\). I sada
print(result)  # 1987 - Significant Others

# Sad kad imamo ono sto hocemo pravimo kod koji ce lop-ati kroz list i promjeniti sve

fixed_titles = []
pattern = re.compile(r'(^[\w ]+) \((\d{4})\)')
for book in titles:
    result = pattern.sub("\g<2> - \g<1>", book)
    fixed_titles.append(result)

fixed_titles.sort()
# ['1978 - Tales of the City', '1987 - Significant Others', '2014 - The Days of Anna Madrigal']
print(fixed_titles)
