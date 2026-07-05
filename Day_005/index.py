# For loop 
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits : 
#     print(fruit)

# Exercise 
students_scores = [150,120,130,140,110,124,135]
# without using loops
# total_scores = sum(students_scores)

# total_score = 0
# for score in students_scores:
#     total_score += score
# print(total_score)

# how to get the max num , theirs as a function called max also 
# max = 0 
# for score in students_scores:
#     if max > score:
#         continue # it means skip and continue to the next num
#     max = score
#     if score > max : max = score # this without using continue 
# print(max)

# range function (start, end and not included, step)
# for num in range(1,100,10):
#     print(num)

# fizzBuzz Exercise
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

# for num in range(1,101):
#     if num % 3 == 0 and num % 5 == 0 :
#         print("FizzBuzz")
#     elif num % 3 == 0 :
#         print("Fizz")
#     elif num % 5 == 0 :
#         print("Buzz")
#     else:
#         print(num)

