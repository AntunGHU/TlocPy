from say_sup import say_sup
def say_hi():
    print(f"HI! My __name__ is {__name__}")
say_hi()
say_sup()

# rezultat bez modificiranja say_sup-a:
# SUP! My __name__ is say_sup
# HI! My __name__ is __main__
# SUP! My __name__ is say_sup

# nakon if-anja
# HI! My __name__ is __main__
# SUP! My __name__ is say_sup