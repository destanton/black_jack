from deck_and_card import Deck, Card, Hand
from players import Player
from players import Dealer
import sys


class Game:
    def setup(self, player, deck):
        self.player = [Player(),
                       Dealer()]
        self.deck = deck

    def hit_or_stand(self):
        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == "h":
            user_hand.add_card(deck.deal_card())
            user_hand.show()
            print(user_hand.get_value())
        else:
            print("Player's hand:")
            print(user_hand.get_value())
            print("Dealer's hand:")
            print(dealer_hand.get_value())
        #     dealer_hand.add_card(deck.deal_card())
        #     dealer_hand.show()

        while True:
            if user_hand.get_value() == 21:
                print("BLACKJACK PLAYER WINS!!!")
                return False
            elif dealer_hand.get_value() == 21:
                print("BLACKJACK DEALER WINS!!!")
                return False
            elif user_hand.get_value() < 16:
                game.hit_or_stand()
                print(user_hand.get_value())
                return False
            elif user_hand.get_value() >= 21:
                print("Game Over! You Busted!")
                return False
            elif user_hand.get_value() >= 16 and dealer_hand.get_value() < 17:
                print("Dealer draws another card")
                dealer_hand.add_card(deck.deal_card())
                print(dealer_hand.get_value())
                # print("Dealer draws another card")
                # print("\n")
                # dealer_hand.add_card(deck.deal_card())
                # print(dealer_hand.show())
                # print(dealer_hand.get_value())
            elif dealer_hand.get_value() >= 21:
                print("Dealer Busts. Player wins!")
                return False
            elif user_hand.get_value() >= dealer_hand.get_value():
                print("Game Over! Player's hand beats the Dealer!")
                return False
            else:
                break    # print(choice)

    def replay(self):
        choice = input("Do you want to play again? [Y]es/n ").lower()
        if choice != "n":
            game()
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
game.hit_or_stand()

# turns []
