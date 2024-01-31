import random

from anyio import sleep


print("Let's play rock, paper, scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'quit' to quit the game.")
user_choice = input("Enter your choice: ")

# Computer's choice
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print("Computer chose:", computer_choice)

if user_choice.lower() == "quit":
    print("Quitting the game...")
    exit()


# Determine the winner
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")

