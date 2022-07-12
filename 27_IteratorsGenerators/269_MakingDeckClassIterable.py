# 2'21

from random import shuffle


class Card:

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())
    
    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        """
        Return a list of cards dealt
        """
        count = self.count()
        actual = min([num, count])  # make sure we don't try to over-deal

        if count == 0:
            raise ValueError("All cards have been dealt")

        if actual == 1:
            return [self.cards.pop()]

        cards = self.cards[-actual:]  # slice off the end
        self.cards = self.cards[:-actual]  # adjust cards

        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")

        shuffle(self.cards)
        return self

    def deal_card(self):
        """
        Returns a single Card
        """
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        """
        Returns a list of Cards
        """
        return self._deal(hand_size)
    
d = Deck()
d.shuffle()
#? card = d.deal_card()
#? print(card)     # Diamonds of Q
#? 
#? hand = d.deal_hand(50)
#? card2 = d.deal_card()
#? print(card2)    # Hearts of 10
#? print(d.cards)  # []
#? card3 = d.deal_card()   # ValueError: All cards have been dealt

# Ako pokusamo sa npr
for card in d:
    print(card) # TypeError: 'Deck' object is not iterable
# razlog je taj da unutar Deck klase nema iter- niti next-dundera koji bi obradjivali iter() inext() pozive for-loop-a. Zato ako ispod __repr__ dundera ugradimo __iter__ Deck klasa postaje iterator.
# Nakon dodanog koda:
#? Spades of 9
#? Diamonds of A
#? Clubs of 5
#? Spades of Q
#? Clubs of 9
#? Spades of 6
#? Hearts of K
#? Hearts of 7
#? Clubs of 2
#? Clubs of 3
#? Diamonds of K
#? Hearts of 3
#? Hearts of 5
#? Diamonds of Q
#? Diamonds of 4
#? Clubs of Q
#? Spades of 4
#? Clubs of 10
#? Spades of 5
#? Clubs of A
#? Spades of A
#? Clubs of J
#? Spades of 7
#? Spades of 10
#? Hearts of 2
#? Diamonds of 3
#? Diamonds of 6
#? Clubs of 4
#? Clubs of 8
#? Hearts of 6
#? Hearts of A
#? Clubs of 6
#? Hearts of Q
#? Hearts of 10
#? Diamonds of J
#? Spades of K
#? Clubs of 7
#? Diamonds of 10
#? Hearts of 9
#? Diamonds of 8
#? Hearts of 8
#? Hearts of J
#? Spades of 8
#? Hearts of 4
#? Spades of 3
#? Diamonds of 7
#? Diamonds of 5
#? Spades of 2
#? Diamonds of 2
#? Diamonds of 9
#? Clubs of K
#? Spades of J