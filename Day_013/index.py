# def print_countdown(start):
#     for i in range(start, 0):  # range never runs backward like this
#         print(i)

# print_countdown(5)  # Expects 5,4,3,2,1 — prints nothing

# solution 
# def print_countdown(start):
#     for i in range(start, 0, -1):  # step -1 needed to count down
#         print(i)

# print_countdown(5)


# def add_item(item, cart=[]):  # default list is shared across calls
#     cart.append(item)
#     return cart

# print(add_item("apple"))   # ['apple']
# print(add_item("banana"))  # ['apple', 'banana']  unexpected

# solution
# def add_item(item, cart=None):
#     if cart is None:
#         cart = []
#     cart.append(item)
#     return cart

# print(add_item("apple")) 
# print(add_item("banana"))

# try:
#     # code that might cause an error
#     result = 10 / 0
# except ZeroDivisionError:
#     # runs only if that specific error happens
    # print("You can't divide by zero!")

# another type of error 
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(result)
# except ValueError:
#     print("That's not a valid number!")
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# to deal any type of error
# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
# except Exception as e:
#     print(f"Something went wrong: {e}")

# example with final keyword
# try:
#     number = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input!")
# else:
#     print(f"You entered {number} — no errors!")  # runs only if try succeeded
# finally:
#     print("This always runs, error or not.")  # runs anyway 

