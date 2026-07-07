from art import logo
from helper_functions import add,subtract,divide,multiply
print(logo)


# without using functions 
to_continue = True
# while to_continue:
#     first_num = float(input("What's the first number?: "))
#     operation = input("""
#     +
#     -
#     *
#     /
#     Pick an operation: 
#     """)
#     second_num = float(input("What's the second number?: "))

#     if operation == "+":
#         print(f"{first_num} + {second_num} = {first_num + second_num}")
#     elif operation == "-":
#         if first_num > second_num:
#             print(f"{first_num} - {second_num} = {first_num - second_num}")
#         else: print(f"{second_num} - {first_num} = {second_num - first_num}")
#     elif operation == "*":
#         print(f"{first_num} * {second_num} = {first_num * second_num}")
#     elif operation == "/":
#         if first_num > second_num:
#             print(f"{first_num} / {second_num} = {first_num / second_num}")
#         else: print(f"{second_num} / {first_num} = {second_num / first_num}")
#     else:
#         print("invalid operation")
    
#     want_to_continue = input("Type 'y' to continue calculating, or type 'n' to end the program: ").lower()
#     if want_to_continue == "y":
#         continue
#     elif want_to_continue == "n":
#         to_continue = False
#         print("GoodBye")
#     else:
#         print("Enter a valid choice")
#         want_to_continue = input("Type 'y' to continue calculating with 2.0, or type 'n' to start a new calculation: ").lower()


# using functions 
while to_continue:
    first_num = float(input("What's the first number?: "))
    operation = input("""
    +
    -
    *
    /
    Pick an operation: """)
    second_num = float(input("What's the second number?: "))

    if operation == "+":
        print(add(first_num, second_num))
    
    elif operation == "-":
        print(subtract(first_num, second_num))
    
    elif operation == "*":
        print(multiply(first_num, second_num))

    elif operation == "/":
        print(divide(first_num, second_num))

    else:
        print("invalid operation")

    want_to_continue = input("Type 'y' to continue calculating, or type 'n' to end the program: ").lower()
    
    if want_to_continue != "y":
        to_continue = False