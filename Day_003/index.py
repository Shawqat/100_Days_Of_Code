# conditions 
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
# comparison operators
# > >= < <= == !=
if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride.")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# nested if statements
is_student = input("Are you a student? (yes/no): ").lower()
if is_student == "yes":
    age = int(input("What is your age? "))
    if age < 18:
        print("You are eligible for a student discount.")
else:
    print("You are not eligible for a student discount.")

# BMI calculator with interpretations
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}. You are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}. You have a normal weight.")
else:
    print(f"Your BMI is {bmi:.2f}. You are overweight.")

# logical operators
# And all conditions must be true, or one condition must be true , not ! reverse
age = int(input("Enter your age: "))
if age >= 18 and age <= 65:
    print("You are eligible for the program.")
else:
    print("You are not eligible for the program.")
