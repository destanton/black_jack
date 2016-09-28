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
            print("BLACKJACK!!! {} is player's score & {} is dealer's score".format(user_hand.get_value(), dealer_hand.get_value()))
            sys.exit()
        elif user_hand.get_value() > 21:
            print("You Busted! ¯\_(ツ)_/¯ ")
            sys.exit()
        elif dealer_hand.get_value() > 21:
            print("You Busted! ¯\_(ツ)_/¯ ")
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
            game.check_dealer()

    def player_turn(self):
        if user_hand.get_value() >= 21:
            game.check_winner()
        elif user_hand.get_value() <= 17:
            game.hit_or_stand()

    def check_dealer(self):
        while dealer_hand.get_value() < 21:
            if dealer_hand.get_value() < 17 or dealer_hand.get_value() < user_hand.get_value():
                dealer_hand.add_card(deck.deal_card())
                dealer_hand.show()
                game.check_winner()
            elif dealer_hand.get_value() == user_hand.get_value():
                dealer_hand.add_card(deck.deal_card())
                dealer_hand.show()
                game.check_winner()
            else:
                game.check_winner()

    def check_winner(self):
        if dealer_hand.get_value() > 21:
            print("You win! Dealer Busted!")
            sys.exit()
        elif user_hand.get_value() > 21:
            print ("You lose! You Busted! ¯\_(ツ)_/¯")
            sys.exit()
        elif user_hand.get_value() == dealer_hand.get_value():
            game.check_dealer()
        elif dealer_hand.get_value() > user_hand.get_value():
            print("DEALER WINS!!!")
            sys.exit()
        elif user_hand.get_value() > dealer_hand.get_value():
            print("You win!")
            sys.exit()

    def replay(self):
        choice = input("Do you want to play again? [Y]es/n ").lower()
        if choice != "n":
            game.replay()
        else:
            print("Bye!")
            sys.exit

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


# print(user_hand.get_value())
# print(dealer_hand.get_value())


game.player_turn()
game.check_dealer()
game.check_winner()
game.replay()
