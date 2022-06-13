# Add up all odd numbers between 10 and 20
# Store the result in x:

x = 0
for n in range(10, 21):
    if n % 2 != 0:
        x += n
print(x)
