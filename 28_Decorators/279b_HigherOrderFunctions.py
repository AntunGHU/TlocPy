from random import choice

# Nested funs inside one another


def greet(person):
    def get_mood():
        msg = choice(('HelloThere!', 'GoAway!', 'I love you!'))
        return msg
    result = person + ', ' + get_mood()
    return result


print(greet("Toby"))


# funs returned from another funs

def make_laugh_func():
    def get_laugh():
        laugh = choice(('hahaha', 'lol', 'tehehe'))
        return laugh
    return get_laugh


l = make_laugh_func()
print(l)  # <function make_laugh_func.<locals>.get_laugh at 0x7f9ad1cae430>
print(l())  # tehehe
# <function make_laugh_func.<locals>.get_laugh at 0x7f5b17f784c0>
print(make_laugh_func())
print(make_laugh_func()())  # tehehe    # nisam ocekivao ovo!!!


# unutrasnja dohvaca argument vanjske

def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('hahaha', 'lol', 'tehehe'))
        return f"{laugh} {person}"
    return get_laugh


laugh_at = make_laugh_at_func("Linda")
print(laugh_at())   # tehehe Linda
print(laugh_at)  # <function make_laugh_at_func.<locals>.get_laugh at 0x7feb5ee77550>
