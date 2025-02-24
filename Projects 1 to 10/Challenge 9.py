"""
Very messy, rudimentary code I was intending to make for Chinese Blackjack or "Ban Luck"
Partially done, I am intending to update this in the future.
"""


import random

deckofcards = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": [1, 10, 11]
}

# function below checks for ace card since ace has a list value
def get_card_value(card):
    if isinstance(card, list):
        return card[-1]
    return card

def newcard(userCards):
    count = 0
    drawn_card = random.choice(list(deckofcards.values()))
    userCards += get_card_value(drawn_card)

    print(f"You drawn {drawn_card}.")

    while userCards < 15:
        choice1 = input("Would you like a card? (y/n): ").strip().lower()

        if choice1 == "y":
            drawn_card = random.choice(list(deckofcards.values()))
            userCards += get_card_value(drawn_card)
            print(f"You drawn {drawn_card}.\n")
            count = 0
        else:
            count += 1
            if count >= 2:
                break
            while count < 2:
                print("You must draw a card.")
                final_choice = input("Draw a card? (y/n): ").strip().lower()
                if final_choice != "y":
                    count += 1
                    return userCards
                else:
                    drawn_card = random.choice(list(deckofcards.values()))
                    userCards += get_card_value(drawn_card)
                    print(f"You drawn {drawn_card}.\n")
                    count = 0

    while userCards < 21:
        choice2 = input(
            f"Would you like another card? You currently have {userCards}. (y/n): " ).strip().lower()

        if choice2 != "y":
            break

        drawn_card = random.choice(list(deckofcards.values()))
        userCards += get_card_value(drawn_card)
        print(f"You drawn {drawn_card}.\n")

        if userCards > 21:
            print("You busted.")
            break

    return userCards

def pc_draw(pcCards):
    while pcCards < 15:
        pc_drawn_card = random.choice(list(deckofcards.values()))
        pcCards += get_card_value(pc_drawn_card)

    while 15 <= pcCards <21:
        if random.choice([True, False]):
            pc_drawn_card = random.choice(list(deckofcards.values()))
            pcCards += get_card_value(pc_drawn_card)
        else:
            break

    return pcCards

userCards = 0
pcCards = 0
userCards = newcard(userCards)
pcCards = pc_draw(pcCards)

if userCards < 15:
    print("Not enough cards. PC wins.")
elif userCards > 21:
    print(f"Final hand value: {userCards}")
    print(f"PC hand value: {pcCards}")
    print("PC wins.")
elif pcCards > 21:
    print(f"Final hand value: {userCards}")
    print(f"PC hand value: {pcCards}")
    print("You win.")
elif userCards > pcCards:
    print(f"Final hand value: {userCards}")
    print(f"PC hand value: {pcCards}")
    print("You win.")
else:
    print(f"Final hand value: {userCards}")
    print(f"PC hand value: {pcCards}")
    print("PC wins.")