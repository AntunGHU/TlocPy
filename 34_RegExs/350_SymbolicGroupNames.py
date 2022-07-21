# 4'21

import re


def parse_name(input):
    name_regex = re.compile(
        r'^(Mrs\.|Ms\.|Mr\.|Mdme\.) (?P<ime>[A-Za-z]+) ([A-Za-z]+)$')
    matches = name_regex.search(input)
    print(matches.groups())
    print(matches.group(2))  # Tilda
    print(matches.group('ime'))  # Tilda


parse_name("Mrs. Tilda Swinton")  # ('Mrs.', 'Tilda', 'Swinton')

# recimo da zelimo samo ime radi npr pozdrava " Helo Tilda". Jedan nacin za dobiti ga je "print(matches.groups(2))"

# drugi nacin je da u grupu () za ime dodamo ala "label"- grupe s imenom "?P<ime>" te pri potivanju kao arg navedemo to ime. Prednost toga je da nema potrebe za brojanjem koja je grupa po redu.
