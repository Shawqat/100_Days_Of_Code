import string
import random

# Password Generator Project
print("Welcome to the PyPaswword Generator")

letters_range = int(input("Hom many letters would you like in your password?: "))
symbole_range   = int(input("How many symboles would you like ?: "))
numbers_range   = int(input("How many numbers would you like ? : "))

letters     = string.ascii_letters # list of letters capital and small 
symboles    = string.punctuation   # list of symboles
numbers     = string.digits        # list of all digit numbers

password_list = []

for letter in range(letters_range):
    password_list.append(random.choice(letters))

for symbole in range(symbole_range):
    password_list.append(random.choice(symboles))

for number in range(numbers_range):
    password_list.append(random.choice(numbers))

random.shuffle(password_list) # to break the consistent of creating password 
password = "".join(password_list) # it's a function that convert list to string
print(f"Your generated Password: {password}")
