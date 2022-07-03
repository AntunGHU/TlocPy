# 10'10''
# na pypi.python.org/pypi se nalaze ext-moduli oko 125000
# colt instalira termcolor sa
#? python3 -m pip install termcolor
# ali nije islo pa sam sa
#? pip3 install termcolor
# i uspio!! ali morao prebaciti na 3.9

# >>> import termcolor
# >>> help(termcolor)

from termcolor import colored
text = colored("Hi there", color="cyan")
print(text)
# prosirenje sa highlightiranjem
text = colored("Hi there", color="yellow", on_color="on_cyan")
print(text)
# prosirenje sa blinkanjem
text = colored("Hi there", color="yellow", on_color="on_cyan", attrs=["blink"] )
print(text)

# QUIZ:
# q1: Syntaksa za import built-insa razlikuje se od one za vlastite py-fajlove? Ne
# q2: Koja se rjec ne koristi pri importanju? export
# q3: Koja je razlika "import random" i "from random import"? sve i dio modula
# q4: Koji ne valja za import: "from some stuff import x as baum"