# primjeri za any i all mogu i bez LC tj [] zagrada. Tada postaju tzv GeneratorExpressions tj objekti puno laksi za RAM. Naravno, tada više nisu primjenjivi list-metodi

import sys
list_comp = sys.getsizeof([x*10 for x in range(1000)])
gen_exp = sys.getsizeof(x*10 for x in range(1000))
print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes") # 8856 bytes
print(f"Generator Expression: {gen_exp} bytes") # 104 bytes