import random
import time

def spin():
    fruits = ['🍒','🍇','🍓','🐶','✨']
    row = []
    for _ in range(3):
        row.append(random.choice(fruits))
    return row

def print_row(row):
    print(f"|{row[0]}|{row[1]}|{row[2]}|")

def evaluate_reward(row, bet):
    if row[0]==row[1]==row[2]:
        if row[0] == '🍒':
            return bet*2
        elif row[0] == '🍇':
            return bet*5
        elif row[0] == '🍓':
            return bet*10
        elif row[0] == '🐶':
            return bet*20
        elif row[0] == '✨':
            return bet*50
        
    return 0

def slot_machine():
    balance = 200

    print(30*'-')
    print("Welcome to python slots")
    print("Symbols: '🍒','🍇','🍓','🐶','✨'")
    print("Are you ready for a big payday?")
    print(30*'-')

    while balance>0:
        print(f"\nYour current balance is {balance} €")

        bet = input("\nPlease place your bet: ")

        if not bet.isdigit():
            print("Not a valid value\n")
            continue

        bet = int(bet)

        if bet>balance:
            print("Not enough balance...\n")
            continue

        if bet<0:
            print("Bet should be greater than zero...\n")
            continue

        balance -= bet
        print(f"Your balance is {balance} €")

        row = spin()
        print("spinning...\n")
        time.sleep(2)

        print_row(row)

        reward = evaluate_reward(row,bet)

        if reward != 0:
            print(f"Congratulations! You win {reward} €\n")
        else:
            print(f"You lost this round. Place another bet or press q to quit...\n")

        balance += reward

        if balance == 0:
            break

        print("Press q to quit, press any other key to continue\n")
        key = input()

        if key == 'q' or key == 'Q':
            break

    print(30*'-')
    print(f"Game over. Your final balance is {balance} €")

if __name__ == "__main__":
    slot_machine()
