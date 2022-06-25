# () u naslovu fajla 198_abs()... dovele do javljanja greske "bash: syntax error near unexpected token `('". Nikakva linija u report-u greske tako da sam to mogao skuziti puno ranije da nije vezano za kod nego naslov!!
import math

print(abs(-5))
print(abs(5))
print(abs(3.45))
print(abs(-5.412))
print(abs(float(3)))
print(abs(int(2.1)))
# import math-a daje novu varijantu "fabs"
print(math.fabs(-4))    # 4.0

# sum prima iterable sa start-value na 0 po def-u i zbraja sve desno
print(sum([1,2,3]))
print(sum([1,2,3], 10))
print(sum([1,2,3], -6))
print(sum((1.21,2.21,3.21)))
# import math-a daje novu varijantu "fsum"
print(math.fsum((1.567,-4.354)))   

# round vraca specificirani broj znamenki. Ako ndigit nije dan vraca integer
print(round(10.212121))
print(round(10.212121, None))
print(round(10.212121, 3))