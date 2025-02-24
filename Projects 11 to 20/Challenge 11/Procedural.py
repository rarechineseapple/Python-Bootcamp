from pkgutil import read_code

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

CHANGE = {
    "b": 1.00,
    "q": 0.25,
    "d": 0.10,
    "n": 0.05,
    "p": 0.01
}

END = False
profit = 0

# 1st step: Checks resources
def check_resources(drink):
    if drink in MENU:
        if resources["water"] < MENU[drink]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return False
        elif resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return False
        elif resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return False

# 2nd step: Asks user for payment
def insert_coins(drink):
    total_inserted = 0.0
    if drink in MENU:
        price = MENU[drink]["cost"]
        print(f"Please pay ${price} ")

    while total_inserted < price:
        inserted = input("Insert money (b = Dollar, q = Quarter, d = Dime, n = Nickle, p = Pennies) ").lower()
        print("Type 'done' if you're finished.")

        if inserted == "done":
            break
        elif inserted in CHANGE:
            total_inserted += CHANGE[inserted]
            print(f"Total inserted: ${total_inserted:.2f}")
        else:
            print("Invalid input. We only accept coins and single dollars.")
            print("Type 'done' if you're finished.")

    if total_inserted >= price:
        change = total_inserted - price
        print(f"Thank you for your purchase. Your change: ${change:.2f} ")
        return price
    else:
        print(f"Insufficient value. Returning your money: ${total_inserted} ")
        return 0

# Step 3: makes the coffee
def make_coffee(drink):
    water = MENU[drink]["ingredients"]["water"]
    milk = MENU[drink]["ingredients"].get("milk", 0)
    coffee = MENU[drink]["ingredients"]["coffee"]

    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

# Step 4(optional): Returns a report
def report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")

#report()

while not END:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee == "report":
        report(profit)
    elif coffee == "off":
        END = True
    elif coffee in MENU:
        if not check_resources(coffee):
            continue
        profit += insert_coins(coffee)
        make_coffee(coffee)
        print(f"Here is your {coffee}. Enjoy!")
    else:
        print("We do not have that item.")


