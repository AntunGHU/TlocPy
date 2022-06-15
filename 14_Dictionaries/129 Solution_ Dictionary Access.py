# This code picks a random food item:
from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"])
print(food)

bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}
# YOUR CODE GOES BELOW:

if food in bakery_stock:
    print(f"We have {food} {bakery_stock[food]} left")
else:
    print("We don't make "+ food)

#! get - rjesenje
kolicina = bakery_stock.get(food)
if kolicina:
    print(f"We have {food} {bakery_stock[food]} left")
else:
    print("We don't make "+ food)