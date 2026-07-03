# Data types, it's how we identify data so that we can use it properly.
# Strings, integers whole numbers , floats decimal numbers , booleans true or false
name = "Mahmoud" # we could use this brackets to select specific string [index]
age  = 28
height = 1.75
is_student = False

print("first letter of ur name : ", name[0])
print(123_135_123) # we can use underscores to make numbers more readable

print(type(is_student)) # using type() to know what's the data type

## type conversion || Casting
print( type( str(age) ) ) # converting integer to string
# we can't convert string chars like (A,B,C) to integer or float
print( type( int(height) ) ) # converting float to integer

# Math operators
# + - * => multiply / % => reminder ** => power // => floor division 
print(6 + 2)
print(6 - 2)
print(6 * 2)
print(6 / 2) # with floating point part.
print(6 // 2) # without floating point part.
print(6 % 2) # remainder
print(2 ** 3) # 2 to the power of 3

print( 2 + 3 * 4 ) # remember pemdas order of operations 

# BMI => Body Mass Index Calculator
weight  = 70 # in kilograms
height  = 1.75 # in meters
bmi     = weight / (height ** 2)
# f-strings let's us embed variables inside strings, also we could do math operations.
print(f"Your BMI is : {round(bmi, 2)}") # round() to round the number to 2 decimal places

# Assignment operators it's a short way to write math operations 
# +=, -=, *=, /=, %=, **=, //=
x = 5
x += 3 # x = x + 3
print(x) 




