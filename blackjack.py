import random

def create_deck():
    suits = ['Clubs','Spades','Hearts','Diamonds']
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','Ace']
    deck = [(value,suit) for value in values for suit in suits]
    random.shuffle(deck)
    return deck

def calculate_hand_value(hand):
    value = 0
    aces = 0

    for card,_ in hand:
        if card in ['J','Q','K']:
            value += 10
        elif card == 'Ace':
            value += 11
            aces += 1
        else:
            value += int(card)
    while value>21 and aces>0:
        value -= 10
        aces -= 1

    return value

def deal_card(deck):
    return deck.pop()

def show_hand(hand,person):
    print(f"{person}'s hand: {','.join([f"{value},{suit}" for value,suit in hand])}")

def black_jack_game():
    print("Welcome to Blackjack")

    deck = create_deck()

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    while True:
        show_hand(player_hand, "Player")

        player_value = calculate_hand_value(player_hand)

        print(f"Your total: {player_value}")

        if player_value > 21:
            print("You busted! Dealer wins!")
            return

        action = input("(H)it or (S)tand? ").strip().lower()

        if action == "h":
            player_hand.append(deal_card(deck))
        elif action == "s":
            break

    print("\nDealer's turn")
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
    show_hand(dealer_hand, "Dealer")
    dealer_value = calculate_hand_value(dealer_hand)
    print(f"Dealer's total: {dealer_value}")

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value == dealer_value:
        print("It's a tie")
    else:
        print("Dealer wins.")

if __name__ == "__main__":
    black_jack_game()
