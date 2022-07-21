# Define a function called parse_date  that accepts a single string.  Your code should check to see if the string matches a date format.  We're going to use the DMY format of "dd/mm/yyyy", but it should also work with "dd.mm.yyyy" and "dd,mm,yyyy". If you are American, note that Day is before Month!  However, rather than simply returning True or False if the string matches...you should instead return a dictionary containing the three parts of the date with the keys "d" , "m" , and "y"  like so:

import re


def parse_date(input):
    pattern = re.compile(r"^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
    match = pattern.search(input)
    if match:
        return {
            "d": match.group(1),
            "m": match.group(2),
            "y": match.group(3),
        }
    return None

#  Note: the string should be an EXACT match, containing the date and nothing else. If there is no match, return None


print(parse_date("12,04,2003"))  # {'d': '12', 'm': '04', 'y': '2003'}
print(parse_date("12.11.2003"))  # {'d': '12', 'm': '11', 'y': '2003'}
print(parse_date("12.11.200312"))  # None
