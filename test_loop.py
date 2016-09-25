def check_winner(self):
    high_range = 21
    low_range = 17

    while True:
        if dealer_hand.get_value() < low_range and dealer_hand.get_value() >= 21 :
            dealer_hand.add_card(deck.deal_card())
            print("Dealer's hand")
            print(dealer_hand.get_value())
        else:
            break
    while True:
        if user_hand.get_value() <= 21 and dealer_hand.get_value() < 21:
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


            def check_winner(self):
                while dealer_hand.get_value() < 17:
                    if user_hand.get_value() <= 21 and dealer_hand.get_value() < 21:
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

                                # else:
                                #     print("Your hand is over 21, you lose")
                                #     print("\n")
                                #     return False

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
