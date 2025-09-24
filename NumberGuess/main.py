#Generates random number
#Ask the user to make guess
#if not a valid number
#print an error
#if number < guess
#print too high
#if number < guess
#print too low
#Else 
#print well done
import random

number_to_guess = random.randint(1, 100)
while True:
    try:
        guess = int(input("Guess the Number Between 1 to 100: "))

        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please Enter a Valid Number!")

