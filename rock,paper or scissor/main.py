import random

choices = ("r", "p", "s")

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s)=> ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid Choice!")

def display_choices(user_choice, computer_choice):
    print(f"You Choose - {user_choice}")
    print(f"Computer Choose - {computer_choice}") 

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == "r" and computer_choice == "s") or
        (user_choice == "s" and computer_choice == "p") or
        (user_choice == "p" and computer_choice == "r")):
        print("You Win")
    else:   
        print("You lose")
            
def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input("Continue? (Y/N) => ").lower()
        if should_continue == "n":
            break
play_game()
