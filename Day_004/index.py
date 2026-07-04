# to get a module that have been installed or built-in 
import random
# we can import whole module or just get a specific function or class from it
# from random import randint
# print(random.randint(1, 10))  # generates a random integer between 1 and 10

# random_number_0_1 = random.random() * 10

# print(random_number_0_1)  # generates a random float between 0 and 1

# random_float = random.uniform(1, 10)  # generates a random float between 1 and 10
# print(random_float)  # generates a random float between 1 and 10

# random_choice = random.randint(0, 1)  # generates a random integer between 0 and 1
# if random_choice == 0:
#     print(f"Heads")
# else:
#     print(f"Tails")

# Lists 
# names = ["Ahmed", 26, True, 1.72]
#         # 0        1    2    3 
# print(f"your name is {names[0]} and your age is {names[1]} and your height is {names[3]}")

# lists are mutable, we can change the values of a list
# lists functions
# Adding
# names.append("Adam") # to the end of list
# names.insert(1, "Sara") # to a specific index 

# Updating
# names[0] = "Ali"

# # Removing 
# names.remove("Ahmed") # removes the first occurrence of the value
# names.pop(2) # removes the element at the specified index
# names.clear() # removes all elements from the list

# Excercise
# frineds = ["Ahmed", "Ali", "Sara"]
# choice = random.randint(0, len(frineds) - 1)
# print(f"{frineds[choice]} is going to buy the meal today!")

# using choice function
# frineds = ["Ahmed", "Ali", "Sara"]
# choice = random.choice(frineds)
# print(f"{choice} is going to buy the meal today!")

# nested Lists
# states_of_Egypt = ["Cairo", "Giza", "Alexandria", ["Asyut", "Luxor", "Hurghada"]]
# print(states_of_Egypt[3][1])  # prints "Luxor"
