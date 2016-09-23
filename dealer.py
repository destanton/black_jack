from hand import Hand
from player import Player


class Dealer(Hand, Player):
    def __init__(self, name, hand):
        self.name = "Dealer"
        self.hand = hand

    def hit(self, deck):
        self.hand.draw(deck)

        
