from deck_and_card import Deck, Card, Hand
from players import Player
from players import Dealer


class Game:
    def setup(self, player, deck):
        self.player = [Player(),
                       Dealer()]
        self.deck = deck

    def hit_or_stand(self):
        choice = input("Do you want to [H]it or [S]tand? ").lower()
        return choice


user = Player("Danielle")
dealer = Player("Dealer")
deck = Deck()
deck.shuffle_deck()
user_hand = Hand(user)
dealer_hand = Hand(dealer)
# card = deck.deal_card()

user_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())
user_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())

print(user_hand.get_value())
print(dealer_hand.get_value())
user_hand.show()
dealer_hand.show()
game = Game()
game.hit_or_stand()

# turns []

# while turns != 4:
    # card is dealt to player
        # turns += 1
    # card is dealt to dealer
        # turns += 1
    # call win check function


# win check function
    # checks players hand for value of cards
        # prints value of cards
        # gives player option to hit or stay
            #if hit then card + 1
                #check total of cards
    # checks dealers hand for value
        #prints value of cards
            # if value < 17
                # hit for another card, check value
