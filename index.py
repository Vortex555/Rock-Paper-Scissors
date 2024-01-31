import random

from anyio import sleep


def play_game():
    print("Let's play rock, paper, scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' to quit the game.")
    user_choice = input("Enter your choice: ")

    # Computer's choice
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if user_choice.lower() == "quit":
        print("Quitting the game...")
        exit()
    else:
        print("Computer chose:", computer_choice)

    # Determine the winner
    if user_choice not in choices:
        print("Please choose a valid option and try again or exit the game.")
        play_game()
    elif user_choice == computer_choice:
        print("It's a tie!")
        play_game()
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        play_game()
    else:
        print("You lose!")
        play_game()


play_game()


