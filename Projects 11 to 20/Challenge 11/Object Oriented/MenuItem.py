from Menu import Menu
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine
from prettytable import PrettyTable

END = False

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
table = PrettyTable()

table.field_names = ["Coffee", "Cost"]
table.add_rows(
    [
        [str(item.name), f"${item.cost}"] for item in menu.menu
    ]
)

print("Coffee Machine Menu:")
print(table)

while not END:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "report":
        coffee_maker.report()
    elif coffee == "profit":
        money_machine.report()
    elif coffee == "off":
        END = True
    else:
        result = menu.find_drink(coffee)

        if result is None:
            continue

        if not coffee_maker.check_resources(result):
            continue

        payment_successful = money_machine.make_payment(result.cost)
        if payment_successful:
            coffee_maker.make_coffee(result)

