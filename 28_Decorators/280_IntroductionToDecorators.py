# 6'20

# Decorator? : funs koja wraps drugu fun i poboljsava je
# ............ oni su primjeri funs viseg reda, dolaze sa @@@@@@@

# Decorator as a function:
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


def greet():
    print("My name is Colt.")


wrapped_greet = be_polite(greet)  # funkcije u ulozi argumenta su bez ()
wrapped_greet()  # Vidi ispod
# _________________What a pleasure to meet you!
# _________________My name is Colt.
# _________________Have a great day!

# sad isto to ali uz upotrebu @decoratora


def be_politee(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


@be_politee         # iako moze bez @ its nice touch, cini suvisnim L19
def greett():
    print("My name is Matt.")


greett()          # What a pleasure to meet you!
# __________________My name is Matt.
# __________________Have a great day!
