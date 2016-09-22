from random import choice
from random import shuffle


class Player:
    def __init__(self, name):
        self.name = name


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        # jack, king, queen is a 10
        # ace is 11


class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Diamonds", "Spades", "Clubs", "Hearts"]
        self.all_cards = []

        for rank in ranks:
            for suit in suits:
                self.all_cards.append(Card(rank, suit))

    def show_card(self):

        for card in self.all_cards:
            print(card.rank, card.suit)

    def shuffle_deck(self):
        shuffle(self.all_cards)
        return self.all_cards

    def deal_card(self):
        pass

        # self.deal =  # need to deal 1 card at a time to dealer and player

        # for x in range(52)
        # card()


user = Player("Danielle")
dealer = Player("Dealer")
deck = Deck()
deck.shuffle_deck()
deck.show_card()
print(user.name)
print(dealer.name)
# print(deck.all_cards)
# card = Card(rank, suit)

# print(card.rank, card.suit)
# print(deck.show_card())
# print(deck.deck)

# print(deck.deck)
