from deck_and_card import Hand, Card


class Player(Hand, Card):
    def __init__(self, name):
        self.name = name
        self.hand = Hand(name)
        # self.value = value
        # self.hand = hand

    def hit(self, deck):
        self.hand.draw(deck)

        if self.hand.get_value() == 21:
            print("BLACKJACK")

            
class Dealer(Player):
    def __init__(self, name):
        self.name = "Dealer"

    def hit(self, deck):
        self.hand.draw(deck)

        if self.hand.get_value() == 21:
            print("BLACKJACK")
