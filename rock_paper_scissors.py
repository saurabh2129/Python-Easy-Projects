import random

user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]

while True:
    user_input = input("Type rock/ paper/ scissors or q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print("Please provide appropriate value next time...")
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors:2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "scissors" and computer_pick == "paper":
        print("User wins!")
        user_wins += 1
        
    elif user_input =="rock" and computer_pick == "scissors":
        print("User wins!")
        user_wins += 1
        
    elif user_input == "paper" and computer_pick == "rock":
        print("User wins!")
        user_wins += 1
        
    else:
        print("Computer wins!!")
        computer_wins += 1

print(f"User win's {user_wins} times.")
print(f"Computer win's {computer_wins} times.")

print("Goodbye!!!")