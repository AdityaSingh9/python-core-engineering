import random

# ASCII Art
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List for computer choice
ls = ["ROCK", "PAPER", "SCISSORS"]

print("Choose 1 for Rock, 2 for Paper or 3 for Scissors: ")
data = int(input())

if data not in (1, 2, 3):
    print("Invalid input, Game Over!")
else:
    computer_choice = random.choice(ls)

    # Map user input to choice
    if data == 1:
        user_choice = "ROCK"
        print("You chose:")
        print(rock)
    elif data == 2:
        user_choice = "PAPER"
        print("You chose:")
        print(paper)
    else:
        user_choice = "SCISSORS"
        print("You chose:")
        print(scissors)

    print("Computer chose:")
    
    if computer_choice == "ROCK":
        print(rock)
    elif computer_choice == "PAPER":
        print(paper)
    else:
        print(scissors)

    # Game Logic
    if user_choice == computer_choice:
        print("It's a Draw!")
    elif (user_choice == "ROCK" and computer_choice == "SCISSORS") or \
         (user_choice == "PAPER" and computer_choice == "ROCK") or \
         (user_choice == "SCISSORS" and computer_choice == "PAPER"):
        print("You Win! ")
    else:
        print("Computer Wins! ")