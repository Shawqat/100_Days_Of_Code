from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game! \n I'm thinking of a number between 1 and 100.")

selected_num = random.randint(1,101)
attempts = 0

def check_user_guess(user_g):
    global attempts
    if user_g == selected_num :
        print("Amazing you got it")
    elif user_g > selected_num:
        print("Too High \nguess again!")
        attempts -= 1
    else:
        print("Too low \nguess again!")
        attempts -= 1

game_level = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
if game_level == "easy":
    attempts = 10
elif game_level == "hard":
    attempts = 5
else:
    print("invalid input!")


while attempts:
    
    user_guess = int(input("Make a guess: "))
    check_user_guess(user_guess)

    if attempts == 0:
        print("=" * 50)
        print(f"You lose , the number was {selected_num}")
        break

    print(f"You have {attempts} attempts remaining to guess the number.\n")