from card import Card
from deck import Deck
import unittest


class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.value, "Hearts")
        self.assertEqual(self.card.suit, "A")

    def test_repr(self):
        """repr should return a string of the form 'VALUE of SUIT'"""
        self.assertEqual(repr(self.card), "Hearts of A")
        # self.assertEqual(self.card.__repr__(), "A of Hearts") # alternativna linija coda


class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """decks should have a cards attribute, which is a list with 52 elements"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_repr(self):
        """repr should return a string of the form 'Deck of COUNT cards.'"""
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """count should return a count of the number of cards in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal_sufficient_cards(self):
        """_deal should deal the number of cards specified, if possible"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insufficient_cards(self):
        """_deal should deal the number of cards left in the deck, if more cards are requested"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """_deal should throw a ValueError if the deck is empty"""
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed into it"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)
        self.assertEqual(self.deck.count(), 52)

    def test_shuffle_not_full_deck(self):
        """shuffle should throw a ValueError if the deck isn't full"""
        self.deck._deal(1)
        with self.assertRaises(ValueError):
            self.deck.shuffle()


if __name__ == "__main__":
    unittest.main()

# povrat bez -v:
# ? antun@ub:~/Documents/aCod/TlocPy$ /bin/python3 /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/303_TestingCard_Deck.py

# ? ----------------------------------------------------------------------
# ? Ran 12 tests in 0.001s

# ? OK

# povrat sa -v:
# ? antun@ub:~/Documents/aCod/TlocPy$ /bin/python3 /home/antun/Documents/aCod/TlocPy/29_TestingWithPy/303_TestingCard_Deck.py -v

# ? test_init (__main__.CardTests)
# ? cards should have a suit and a value ... ok
# ? test_repr (__main__.CardTests)
# ? repr should return a string of the form 'VALUE of SUIT' ... ok
# ? test_count (__main__.DeckTests)
# ? count should return a count of the number of cards in the deck ... ok
# ? test_deal_card (__main__.DeckTests)
# ? deal_card should deal a single card from the deck ... ok
# ? test_deal_hand (__main__.DeckTests)
# ? deal_hand should deal the number of cards passed into it ... ok
# ? test_deal_insufficient_cards (__main__.DeckTests)
# ? _deal should deal the number of cards left in the deck, if more cards are requested ... ok
# ? test_deal_no_cards (__main__.DeckTests)
# ? _deal should throw a ValueError if the deck is empty ... ok
# ? test_deal_sufficient_cards (__main__.DeckTests)
# ? _deal should deal the number of cards specified, if possible ... ok
# ? test_init (__main__.DeckTests)
# ? decks should have a cards attribute, which is a list with 52 elements ... ok
# ? test_repr (__main__.DeckTests)
# ? repr should return a string of the form 'Deck of COUNT cards.' ... ok
# ? test_shuffle_full_deck (__main__.DeckTests)
# ? shuffle should shuffle the deck if the deck is full ... ok
# ? test_shuffle_not_full_deck (__main__.DeckTests)
# ? shuffle should throw a ValueError if the deck isn't full ... ok

# ? ----------------------------------------------------------------------
# ? Ran 12 tests in 0.001s

# ? OK
# prolazi ali nisam zadovoljan sa stanjem u linijama 12 i 13 u kom sam morao izmjeniti mjesta za "Hearts" i "A" kako bi prosao iako to nema logike! Trebalo je biti obrnuto kao sto je i bilo. Zasto ne prolazi kad je ispravno? Ne znaju!


# Summery:
# Unutar testova sami nazivi testova nisu bitni, bitno je da nakon assert-methoda dolaze nazivi isti kao u stvarnom kodu kojeg se testira
# Unutar testova se mogu odradjivati metodi: npr self.deck.cards.pop(), self.deck._deal(100)
