import random

def game_menu():
    while True:
        print("\n1. Number Guessing Game")
        print("2. Rock-Paper-Scissors")
        print("3. Dice Roll Simulation")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            target = random.randint(1, 100)
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == target:   
                print("You won!")
            else:
                print("Try Again")
        elif choice == 2:
            user_choice = input("Enter Rock, Paper, or Scissors: ").lower()
            options = ["rock", "paper", "scissors"]
            computer_choice = options[random.randint(0, 2)]
            if user_choice == computer_choice:
                print("It's a tie!")
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "scissors" and computer_choice == "paper") or \
                 (user_choice == "paper" and computer_choice == "rock"):
                print("You win!")
            else:
                print("Computer wins!")
        elif choice == 3:
            dice = random.randint(1, 6)  
            print("Dice rolled:", dice)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")
 
x=input("Can we play some games?? (type yes and no)")
if x.lower()=="yes":
    game_menu()
else:
    print("Okey , let's play later!")
 


 
