import random

print("\n*** Rock, Paper, Scissors ***\n")

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

art = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors
}

options = ["rock", "paper", "scissors"]

user = input("Choose an option (rock, paper, or scissors): ").strip().lower()

if user not in options:
    print("Please choose rock, paper, or scissors")
else:
    computer = random.choice(options)
    
    print(f"\nComputer chose: {computer}")
    print(art[computer])

    print(f"\nYou chose: {user}")
    print(art[user])

    if computer == user:
        print("It's a tie!")
        
    elif (computer == "rock" and user == "scissors") or (computer == "paper" and user == "rock") or (computer == "scissors" and user == "paper"): 
        print("Computer wins")
    
    else:
        print("You win!")