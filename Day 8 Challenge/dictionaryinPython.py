# Dictionary reference coding

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#printing keys in dictionary "travel_log"
for key in travel_log:
    print(key)

#printing values in dictionary "travel_log"
for values in travel_log:
    print(travel_log[values])

#printing out specific values
print(travel_log["France"][1])

# Getting value from nested list
nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

# example
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {
    'Outstanding': (91, 100),
    'Exceeds Expectations': (81, 90),
    'Acceptable': (71, 80),
    'Fail': (0, 70)
}

graded_students = {}

for student, score in student_scores.items():
    for grade, (low, high) in student_grades.items():
        if low <= score <= high:
            graded_students[student] = grade

for student, grade in graded_students.items():
    print(f"{student}: {grade}")

#  If Else
# # Loop through each key in the student_scores dictionary
# for student in student_scores:
#
# # Get the value (student score) by using the key each time.
#     score = student_scores[student]
#
# # Check what grade the score would get, then add it to student_grades
#     if score >= 91:
#         student_grades[student] = 'Outstanding'
#     elif score >= 81:
#         student_grades[student] = 'Exceeds Expectations'
#     elif score >= 71:
#         student_grades[student] = 'Acceptable'
#     else:
#         student_grades[student] = 'Fail'

# dictionary with multiple key value pairs

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])

# cities_visited is a key so we must type the key itself out.

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2]) # Retrieves value associated with key 2
print(order["main"][2][0]) # Retrieves the STRING instead.

# Adding to a dictionary

dict = {
    1: "Apple",
    2: "Pear",
    3: "Strawberry"
}

dict["What"] = "Alien"
print(dict)
