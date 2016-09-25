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
        while True:
            if user_hand.get_value() == 21:
                print("BLACKJACK PLAYER WINS!!!")
                sys.exit()
            elif dealer_hand.get_value() == 21:
                print("BLACKJACK DEALER WINS!!!")
                sys.exit()
            elif user_hand.get_value() > 21:
                print("You Busted!")
                sys.exit()
            else:
                return False

    def hit_or_stand(self):
        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == "h":
            user_hand.add_card(deck.deal_card())
            user_hand.show()
            print("\n")
            print("Your new total is {} ".format(user_hand.get_value()))
            game.player_turn()
        else:
            print("Dealer Draws...")
            game.check_dealer()

    def player_turn(self):
        high_range = 21
        low_range = 17
        while True:
            if user_hand.get_value() >= high_range:
                game.check_winner()
            elif user_hand.get_value() <= low_range:
                game.hit_or_stand()

    def check_dealer(self):
        high_range = 21
        mid_range = 18
        low_range = 17

        while True:
            if dealer_hand.get_value() <= mid_range:
                dealer_hand.add_card(deck.deal_card())
                print("Dealer's hand:")
                # dealer_hand.show()
                print(dealer_hand.get_value())
            else:
                game.check_winner()

    def check_winner(self):
        high_range = 21
        low_range = 17

        while True:
            if dealer_hand.get_value() > high_range:
                print("You win! Dealer Busted!")
                sys.exit()
            # elif user_hand.get_value() < high_range:
            #     game.hit_or_stand()
            elif user_hand.get_value() > high_range:
                print ("You lose! You Busted")
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
            Game()
        else:
            print("Bye!")
            sys.exit


user = Player("Danielle")
dealer = Player("Dealer")
deck = Deck()
deck.shuffle_deck()
user_hand = Hand(user)
dealer_hand = Hand(dealer)
# card = deck.deal_card()
print("{}'s hand is".format("Your"))
user_hand.add_card(deck.deal_card())
user_hand.add_card(deck.deal_card())
user_hand.show()
print("\n")
print("{}'s hand is".format("Dealer"))
dealer_hand.add_card(deck.deal_card())
dealer_hand.add_card(deck.deal_card())
dealer_hand.show()
print("\n")
# print(user_hand.get_value())
# print(dealer_hand.get_value())
game = Game()
# while True:
#     if user_hand.get_value() < 21:
#         game.hit_or_stand()
#     elif user_hand.get_value() > 21:
#         print("Game Over! You Busted!")
#         break
#     # elif dealer_hand.get_value() < 16:
#     #     dealer_hand.add_card(deck.deal_card())
#     # elif dealer_hand.get_value() > 21:
#     #     print("Dealer Busts. Player wins!")
#     #     break
#     else:
#         break

game = Game()
game.check_blackjack()
game.hit_or_stand()
game.player_turn()
game.check_dealer()
game.check_winner()
game.replay = Game()
