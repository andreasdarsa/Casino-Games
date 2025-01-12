import random as rnd

def roll_dice():
    die1 = rnd.randint(1,6)
    die2 = rnd.randint(1,6)
    return die1,die2

def play_turn(player_name):
    print(f"{player_name}'s turn")
    total_score = 0
    for i in range(0,3):
        input("Press enter to roll the dice.")
        print(f"\nRoll no.{i+1}/3:")
        die1,die2 = roll_dice()
        print(f"You rolled {die1} and {die2}.")
        total_score += die1+die2
        if die1 == die2 == 6:
            print("DOUBLE SIXES!!! 10 BONUS POINTS")
            total_score += 10
        if die1 == die2 == 1:
            print("SNAKE EYES! 5 POINTS DEDUCTED")
            total_score -= 7 # 2 points from the roll don't count + 5 points deducted
        print(f"Current Score: {total_score} points.")
    print(f"\nTotal score: {total_score} points.\n")

    return total_score

def dice_game():
    print("🎲 Welcome to Python Dice! 🎲")
    print("Each player rolls the dice 3 times. The player with the highest total score wins.")

    num_players = int(input("Enter the number of players: "))
    player_names = []
    for i in range(num_players):
        name = input(f"Enter player name no. {i+1}: ")
        player_names.append(name)

    scores = {}
    for n in player_names:
        scores[n] = play_turn(n)

    print("\nFINAL SCORES:")
    for name, score in scores.items():
        print(f"{name}: {score} points")

    winner = max(scores, key=scores.get)
    print(f"\n🏆 {winner} wins with {scores[winner]} points! 🏆")


if __name__ == "__main__":
    dice_game()