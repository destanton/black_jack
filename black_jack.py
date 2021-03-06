from deck_and_card import Deck, Card, Hand
from players import Player
from players import Dealer
import sys


class Game:
    def setup(self, player, deck):
        self.player = [Player(),
                       Dealer()]
        self.deck = deck

    def check_blackjack(self):
        if user_hand.get_value() == 21 or dealer_hand.get_value() == 21:
            print("OH SNAP! BLACKJACK!!! The player's score is {} & the dealer's score is {}!".format(user_hand.get_value(), dealer_hand.get_value()))
            sys.exit()
        elif user_hand.get_value() > 21:
            print("YOU BUSTED! ¯\_(ツ)_/¯ ")
            sys.exit()
        elif dealer_hand.get_value() > 21:
            print("DEALER BUSTED! ¯\_(ツ)_/¯ ")
            sys.exit()
        else:
            game.hit_or_stand()

    def hit_or_stand(self):
        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == "h":
            user_hand.add_card(deck.deal_card())
            user_hand.show()
            print("\nYour new total is {} \n".format(user_hand.get_value()))
            game.player_turn()
        else:
            print("\nDealer's Turn!\n")
            game.check_dealer()

    def player_turn(self):
        if user_hand.get_value() > 21:
            game.check_winner()
        elif user_hand.get_value() <= 17:
            game.hit_or_stand()

    def check_dealer(self):
        while dealer_hand.get_value() < 21:
            if dealer_hand.get_value() < 17 or dealer_hand.get_value() < user_hand.get_value():
                dealer_hand.add_card(deck.deal_card())
                # dealer_hand.show()
                # game.check_winner()
            elif dealer_hand.get_value() == user_hand.get_value():
                dealer_hand.add_card(deck.deal_card())
                dealer_hand.show()
                game.check_winner()
        else:
            dealer_hand.show()
            game.check_winner()

    def check_winner(self):
        if dealer_hand.get_value() > 21:
            print("\nYOU WIN! DEALER BUSTED!\n")
            sys.exit()
        elif user_hand.get_value() > 21:
            print ("\nYOU LOSE! YOU BUSTED! ¯\_(ツ)_/¯\n")
            sys.exit()
        elif user_hand.get_value() == dealer_hand.get_value():
            print("\nIT'S A TIE! DEALER WINS!\n")
            sys.exit()
        elif dealer_hand.get_value() > user_hand.get_value():
            print("\nDEALER WINS!!!\n")
            sys.exit()
        elif user_hand.get_value() > dealer_hand.get_value():
            print("\nYOU WIN!\n")
            sys.exit()

# game = Game()
while True:
    game = Game()
    user = Player("Danielle")
    dealer = Player("Dealer")
    deck = Deck()
    deck.shuffle_deck()
    user_hand = Hand(user)
    dealer_hand = Hand(dealer)

    print("{}'s hand is".format("Your"))
    user_hand.add_card(deck.deal_card())
    user_hand.add_card(deck.deal_card())
    user_hand.show()
    print("\n{}'s hand is".format("Dealer"))
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.show()
    print("\n")
    game.check_blackjack()
    game.hit_or_stand()


    game.player_turn()
    game.check_dealer()
    game.check_winner()
    # game.replay()
