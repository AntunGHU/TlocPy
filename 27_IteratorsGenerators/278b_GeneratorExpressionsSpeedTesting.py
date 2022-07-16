# korist od GE amo vec vidjeli kod npr sum-funkcije gdje mozemo i sa LC i sa GE:
import time

from regex import P

print(sum([num for num in range(1, 10)]))  # 45
print(sum(num for num in range(1, 10)))  # 45

# razlika u brzini pri koristenju LC i GE vidi se koristenjem modula "time" (ima i preciznijih!)

gen_start_time = time.time()
print(sum(n for n in range(10000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum(n for n in range(10000000)))
list_time = time.time() - list_start_time

# sum(n for n in range(10000000)) took:0.3782508373260498
print(f"sum(n for n in range(10000000)) took:{gen_time}")
# sum([n for n in range(10000000))] took:0.4062056541442871
print(f"sum([n for n in range(10000000))] took:{list_time}")

# dakle, osim sto GE uzima manje mem u sum-fun je i znatno brzi
