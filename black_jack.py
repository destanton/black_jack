from deck_and_card import Deck, Card, Hand
from players import Player
from players import Dealer
import sys
import random


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
            else:
                return False

    def hit_or_stand(self):
        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == "h":
            user_hand.add_card(deck.deal_card())
            user_hand.show()
            print("\n")
            print("Your new total is {} ".format(user_hand.get_value()))
        else:

            game.check_winner()
    


        #     dealer_hand.add_card(deck.deal_card())
        #     dealer_hand.show()

    def check_winner(self):
        # while True:
            if user_hand.get_value() <= 21 and dealer_hand.get_value() != 21:
                dealer_hand.add_card(deck.deal_card())
                print("Dealer's hand")
                print(dealer_hand.get_value())
                # game.hit_or_stand()
                # return False
            elif dealer_hand.get_value() == 21 and user_hand.get_value() < 21:
                print("Dealer WINS")
                # return False
            elif dealer_hand.get_value() > 21 and user_hand.get_value() < 21:
                print("You win! Dealer went over 21")
                # return False
            elif user_hand.get_value() > 21 and dealer_hand.get_value() <= 21:
                print ("You lose! You went over 21")
                # return False
            else:
                print("Your hand is over 21, you lose")
                print("\n")
                # return False

            # elif user_hand.get_value() < 16:
            #     game.hit_or_stand()
            #     print(user_hand.get_value())
            #     return False
            # elif user_hand.get_value() >= 21:
            #     print("Game Over! You Busted!")
            #     return False
            # elif user_hand.get_value() >= 16 and dealer_hand.get_value() < 17:
            #     print("Dealer draws another card")
            #     dealer_hand.add_card(deck.deal_card())
            #     print(dealer_hand.get_value())
            #     # print("Dealer draws another card")
            #     # print("\n")
            #     # dealer_hand.add_card(deck.deal_card())
            #     # print(dealer_hand.show())
            #     # print(dealer_hand.get_value())
            # elif dealer_hand.get_value() >= 21:
            #     print("Dealer Busts. Player wins!")
            #     return False
            # elif user_hand.get_value() >= dealer_hand.get_value():
            #     print("Game Over! Player's hand beats the Dealer!")
            #     return False
            # else:
            #     break    # print(choice)

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
game.check_winner()
game.replay = Game()

# turns []
