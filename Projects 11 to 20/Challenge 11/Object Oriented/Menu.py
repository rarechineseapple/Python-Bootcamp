class MenuItem:
    # Intializer(constructor) method
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


# Models the Menu with drinks
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    # Returns all the names of the available menu items
    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    # Searches the menu for a particular drink by name
    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print("We do not have that item.")
