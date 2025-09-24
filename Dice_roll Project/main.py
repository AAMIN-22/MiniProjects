# Ask from your roll the dice ?
# if user enter y
# Generates two random numbers
# print them
#if user enter n
# print thank you for playing
# terminate
# else 
# print invalid choice 
import random 
 
while True:
    choice = input("Roll The Dice ? (y/n): ").lower() 
    if choice == "y":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice == "n":
        print("Thank For Playing!")
        break
    else:
        print("Invalid Choice!")