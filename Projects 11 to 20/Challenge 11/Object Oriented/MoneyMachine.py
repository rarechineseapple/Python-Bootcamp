class MoneyMachine:

    CURRENCY = "$"

    CHANGE = {
        "bucks": 1.00,
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.total_inserted = 0

    # Prints the current profit
    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit:.2f}")

    # Returns the total calculated from coins inserted
    def insert_coins(self, cost):
        print("Insert money.")

        while self.total_inserted < cost:
            print(f"Current total: {self.CURRENCY}{self.total_inserted:.2f}")

            for coin, value in self.CHANGE.items():
                amount = int(input(f"How many {coin}: "))
                self.total_inserted += amount * value
                print(f"Current total: {self.CURRENCY}{self.total_inserted:.2f}")


                if self.total_inserted >= cost:
                    break

        return self.total_inserted

    #  Returns True when payment is accepted, or False if insufficient.
    def make_payment(self, cost):
        self.insert_coins(cost)
        if self.total_inserted >= cost:
            change = round(self.total_inserted - cost, 2)
            print(f"Thank you for your purchase. Your change: {self.CURRENCY}{change}")
            self.profit += cost
            self.total_inserted = 0
            return True
        else:
            print("Insufficient value. Returning your money.")
            self.total_inserted = 0
            return False

