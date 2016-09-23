from deck_and_card import Hand, Card


class Player(Hand, Card):
    def __init__(self, name):
        self.name = name
        self.hand = Hand(name)
        # self.value = value
        # self.hand = hand

    def hit(self, deck):
        self.hand.draw(deck)

    def show_hand(self):
        print("{}'s hand: {} {}".format(self.name, self.hand, self.value))
  

class Dealer(Player):
    def __init__(self, name):
        self.name = "Dealer"
