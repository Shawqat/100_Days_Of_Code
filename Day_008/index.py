# def greet(name): # parameter
#     print(f"Hello {name}")

# greet("Mahmoud") # argument

# Exercise how many weeks left if we gonna live for 90y
# def life_in_weeks(age):
#     print(f"You have {(90 - age) * 52} weeks left.")

# life_in_weeks(56)

# positional vs keyword args
# in positional order manner, keyword not 
# def great_with(name, location):
#     print("Hello ", name)
#     print(f"What's like in the {location}")

# great_with("Moud", "Egypt")
# great_with("Egypt", "Moud") positional 

# keyword
# def great_with(name, location):
#     print("Hello ", name)
#     print(f"What's like in the {location}")

# great_with(name="Ahmed", location="Egypt")
# great_with(location="Egypt", name="Ahmed")


# solution 1
# def calculate_love_score(name_1, name_2):
#     first_part = "true"
#     second_part = "love"
#     score_1 = 0
#     score_2 = 0
#     full_name = (name_1 + name_2).lower()
#     for letter in first_part:
#         if letter in full_name:
#             score_1 += full_name.count(letter)
    
#     for letter in second_part:
#         if letter in full_name:
#             score_2 += full_name.count(letter)

#     print(f"{score_1}{score_2}")

# calculate_love_score("Angela Yu", "Jack Bauer")

# solution num 2
# def calculate_love_score(name_1, name_2):
#     full_name = (name_1 + name_2).lower()
#     true_score = sum("true".count(c) for c in full_name)
#     love_score = sum("love".count(c) for c in full_name)
#     print(f"{true_score}{love_score}")
# calculate_love_score("Angela Yu", "Jack Bauer")