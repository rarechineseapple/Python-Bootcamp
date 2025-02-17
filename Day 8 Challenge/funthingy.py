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