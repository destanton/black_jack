from random import choice
from random import shuffle
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suit = ["Diamond", "Spades", "Club", "Heart"]


class Player:
    def __init__(self, name):
        self.name = name


class Card:

    def __init__(self, rank, suit):
        self.rank = choice(rank)
        self.suit = choice(suit)
        # jack, king, queen is a 10
        # ace is 11


# class Deck:
#     def __init__(self, card, rank, suit):
#         self.deck = []
#
#         for rank in rank:
#             for suit in suit:
#                 deck.append(rank, suit)
#
#     def shuffle_deck(self):
#         self.shuffle = shuffle_deck
        # self.deal = # need to deal 1 card at a time to dealer and player

    # for x in range(52)
    # card()

user = Player("Danielle")
dealer = Player("Dealer")
card = Card(rank, suit)

print(user.name)
print(dealer.name)
print(card.rank, card.suit)
