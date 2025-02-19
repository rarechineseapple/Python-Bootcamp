# Fun nested loop thingy I thought i could use as a reference for future coding challenges.

def calculate_love_score(name1, name2):
    name3 = (name1 + name2).upper()
    counter1 = 0
    counter2 = 0

    array1 = ["T", "R", "U", "E"]
    array2 = ["L", "O", "V", "E"]

    for i in name3:
        for j in array1:
            if i == j:
                counter1 += 1
        for k in array2:
            if i == k:
                counter2 += 1

    result = int(f"{counter1}{counter2}")
    return result

    # Alternative solution with lesser lines
    # name3 = (name1 + name2).upper()
    #
    # counter1 = sum(name3.count(letter) for letter in "TRUE")
    # counter2 = sum(name3.count(letter) for letter in "LOVE")
    #
    # result = int(str(counter1) + str(counter2))
    # return result


print(calculate_love_score("John Pork", "Sebastian Lee"))

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

# mini program to showcase dictionary in use

def clear_console():
    print("\n" * 100)

print(art.logo)

bidders = {}

highest_bid = 0
winner = ""

end = False
while not end:

    name = input("What is your name? ")
    bid = float(input("What is your bid? "))

    bidders[name] = bid
    continue_bidding = input("Anymore bidders? Type yes or no: ")
    if continue_bidding.strip().lower() == "yes":
        clear_console()
    else:
        for name, bid in bidders.items():
            if bid > highest_bid:
                winner = name
                highest_bid = bid
        print(f"The winner is {winner} with a bid of ${highest_bid:.2f}.")
        break
    #print(bidders)
	
# Caesar Cipher

import string

alphabet = string.ascii_lowercase #alphabet list

def caesar(encode_decode, original_text, shift_amount):

    result = ""

    if encode_decode == "decode":
        shift_amount *= -1

    for i in original_text:
        if i in alphabet:
            num = alphabet[alphabet.index(i.lower()) + shift_amount]
            if i.isupper():
                result += num.upper()
            else:
                result += num
        else:
            result += i

    print(f"Here is the text: {result}")

end = False
while not end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in["encode", "decode"]:
        print("Invalid input! Please indicate if you want to ENCODE or DECODE.\n")
        continue

    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n")) % 26
    except ValueError:
        print("Invalid input! Please enter an integer value.\n")
        continue

    caesar(encode_decode=direction, original_text=text, shift_amount=shift)

    restart = input("Type yes if you want to use the cipher again.")
    if restart.strip().lower() == "yes":
        continue
    else:
        break