# Class inheritance example

class animal:

    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale and Exhale")

    def move(self):
        print("Moving around by")


class human(animal):

    def __init__(self):
        super().__init__() # inherits attributes from parent class with super function
        self.legs = 2 # attributes of human class

    def walk(self):
        super().move() # Extending the functionality of the move method in parent class
        print(f"Walking with {self.legs} legs.")

Sebastian = human()
# The object can also use the methods of the parent class as it was inherited as well
Sebastian.walk()
Sebastian.breathe()
print(f"He has {Sebastian.num_eyes} eyes.") # Attributes from parent class are manually accesible

# call to super() in the initialiser is recommended, but not strictly required