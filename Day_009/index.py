# Dictionaries key:value pairs
learning = {
    "Html": "structure of the webpage",
    "Css" : "style our webpage",
    "Js"  : "interactive to our webpage",
    "student_active": True,
    "student_age" : 29
}

# print(learning["student_age"]) # bracket notation , dot notation learning.student_age
# learning["test"] = "testing" # you can edit in the same way
# del learning["student_age"] to remove an item 
# print(learning)

# Exercise
# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for key, value in student_scores.items():
#     if value >= 91:
#         student_grades[key] = "Outstanding"
#     elif value >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif value >= 71:
#         student_grades[key] = "Acceptable"
#     else:
#         student_grades[key] = "Fail"

# print(student_grades)

# nesting
# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin"
# }

# travel_log = {
#     "France" : ["Paris", "Lille", "Dijon"],
#     "Germany" : ["Stuttgart", "Berlin"]
# }

# print(travel_log["France"][1]) # lille

# employees = {
#     "emp1": {"name":"Ahmed", "Age":30, "Email":"t@gmail.com"},
#     "emp2": {"name":"Sayed", "Age":20, "Email":"t2@gmail.com"},
#     "emp3": {"name":"Ali", "Age":33, "Email":"t3@gmail.com"},
# }

# print(employees["emp1"]["name"])

