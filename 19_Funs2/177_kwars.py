# **kwargs - spec operator we can pass to funcs; gathers remaining arguments as dictionary; parameter! we can call it we want it!

def fav_colors(**kwargs):
    print(kwargs)
    
fav_colors(Colt="purple", Rubby="red",  Ethel="yellow") #  u bilj stavio sve pod navodne i imao probleme sve dok nisam pogledao video. Ipak Key word znaci key word i ne moze biti pod navodnicima


def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favourite col or is {color}")
        
fav_colors(Colt="purple", Rubby="red",  Ethel="yellow")


def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"]=="special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return "Not sure who this is..."

print(special_greeting(David="Hello"))
print(special_greeting(Bob="Hello"))
print(special_greeting(David="special"))
print(special_greeting(Heather="hello", David="special"))
    