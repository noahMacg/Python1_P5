# MacGillivrayP5
# Programmer: Noah MacGillivray
# EMail: nmacgillivray@cnm.edu
# Purpose: Create rock, paper, scissors game

print("------Welcome to (block) ROCK (in'), PAPER, SCISSORS (beats)------")
print("Be prepared to Dig Your Own Hole")
print("The best rock paper scissors game since 97'\n")

import random

user_input = ""
# Holds game results
# User input is 0 index and comp is 1
game_results = [0, 0]
# Computer list of game moves
comp_choices = ["rock", "paper", "scissors"]
# String to use for each round print
round_start = 'Enter "rock" "paper" or "scissors": '


# Function to check for the round winner
# Also returns the winner of the round
def check_round_win(user_input, comp_move):
    # Checks for draw
    if user_input == comp_move:
        return "DRAW"
    # Check for user_input round win
    elif (
        (user_input == "rock" and comp_move == "scissors")
        or (user_input == "paper" and comp_move == "rock")
        or (user_input == "scissors" and comp_move == "paper")
    ):
        game_results[0] += 1
        return "YOU"
    # If user did not win, computer wins round
    else:
        game_results[1] += 1
        return "ME"


# Game loop that continues as long as the user input is not "no"
while user_input != "no":
    # User's move
    user_input = input(round_start).strip().lower()
    # computer move
    comp_move = random.choice(comp_choices)
    # Uses check_round_win function to check for round winner
    # and sets the round_winner
    round_winner = check_round_win(user_input, comp_move)

    print(f"Computer chose: {comp_move}")
    print(f"You chose: {user_input}")
    print(f"Winner of that round: {round_winner}")
    print(f"Current score: \nYOU- {game_results[0]} \nME- {game_results[1]}\n")
    # Checks for a game winner and restarts / quits the game
    if game_results[0] == 2 or game_results[1] == 2:
        if game_results[0] > game_results[1]:
            print(f"You win this game!")
        else:
            print("I win this game...")
        # Reset the game score
        game_results = [0, 0]

        user_input = (
            input("Would you like to play another game? (select yes/no)")
            .strip()
            .lower()
        )
        print()

print("Thanks for playing!")
