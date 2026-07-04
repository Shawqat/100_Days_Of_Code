# rock_paper_scissors game
import random
print("Welcome to Rock, Paper, Scissors!")
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

choices = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

# test = [1,2,4, "test"]
# print(test.index("test")) # 3
user_choice = int(input())

if user_choice < 0 or user_choice > 2:
    print("Invalid choice. Please choose 0, 1, or 2.")

elif user_choice == 0:
    print("You chose Rock")
    print(choices[0])

elif user_choice == 1:
    print("You chose Paper")
    print(choices[1])

else:
    print("You chose Scissors")
    print(choices[2])

print("\n", "=" * 20)

pc_choice = random.choice(choices)
pc_choice_index = choices.index(pc_choice)

if pc_choice_index == 0:
    print("Computer chose Rock")

elif pc_choice_index == 1:
    print("Computer chose Paper")

elif pc_choice_index == 2:
    print("Computer chose Scissors")

# i believe it would never be executed! :D 
else:
    print("Computer chose an invalid option")

print(choices[pc_choice_index])

# my solution
if user_choice == pc_choice_index:
    print("It's a draw!")

elif (user_choice == 0 and pc_choice_index == 2) or \
     (user_choice == 1 and pc_choice_index == 0) or \
     (user_choice == 2 and pc_choice_index == 1):
    
    print("You Win!")

else:
    print("You Lose!")
