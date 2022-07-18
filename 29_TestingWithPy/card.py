from random import shuffle


class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

c1 = Card("A", "Hearts")
c2 = Card("10", "Diamonds")
c3 = Card("K", "Spades")

print(c1, c2, c3)   # A of Hearts 10 of Diamonds K of Spades