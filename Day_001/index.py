# Write my first python script
print("Hello World!")

# \n to create a new line in the same print statement
print("Hello World!\nThis is my first python script.")

# we can use + to combine strings 
print("Hello " + "World!")

# note : Python case sensitive to spaces and identation
#  print("Hello World!")  # This is would throw an error 

# input function to take user input 
name = input("What is your name? ")
print("Hello " + name + "!")

# (len) this function gives us length of the string
# (str) this function converts a value to a string, to avoid an error
print("The length of your name is: " + str(len(name)))

# variable naming rules : to start with letters or underscore
# it can't have a space in between, it can't contain symbols
# it can't be words that python uses like print, input, str, len, etc.
# also variables case sensitive which means name and Name are different.