# 3'42

# Anchors and Boundaries
# ?     ^	Start of string or line
# ?     $	End of string or line
# ?     \b	Word boundary

# ^\d{3} \d{3}-?\d{4} = 412 412-8765 ali ne i aaa412 412-8765
# \d{3} \d{3}-?\d{4}$ = aaa412 412-8765 ali ne i 412 412-8765abc
# ^\d{3} \d{3}-?\d{4}$ = 412 412-8765 ne aa412 412-8765 ne 412 412-8765asd
# \b\w+\b = hello world i am typing stuff (1. i zadnja rjec nemaju space)
