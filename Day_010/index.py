# def return_double(num):
#     return num * num

# output = return_double(2)
# print(output)

# exercise 
# def format_name(name):
#     # return name.capitalize() # to make the first letter capital 
#     return name.title() # to make first letter of each word capital

# print(format_name("mahmoud khalid"))

# def is_leap_year(year):
#     # always go from specific to general 
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False

# print(is_leap_year(2020))

# Docstrings
# def format_name(name):
#     """
#     - Takes a name parameter : user-name -> String
#     - return name titles -> String
#         ex : mahmoud khalid -> Mahmoud Khalid
#     """
#     return name.title()

# print(format_name("ahmed khalid"))
