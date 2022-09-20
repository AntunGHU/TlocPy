from itertools import count


def single_letter_count(string, letter):
    return string.lower().count(letter.lower())


print(single_letter_count("Hello World", "h"))  # 1
print(single_letter_count("Hello World", "z"))  # 0
print(single_letter_count("HelLo World", "l"))  # 3
print(single_letter_count("single_letter_count", "l"))  # 3


def broj_slova(rjec, slovo):
    c = rjec.lower().count(slovo.lower())
    if c > 0:
        return c
    return "Trazenog slova nema u datoj rjeci!"


print(broj_slova("akapulko", "a"))
