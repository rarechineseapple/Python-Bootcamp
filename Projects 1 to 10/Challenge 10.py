"""
Today I made this program to tackle namespaces and scope.
Python does not have block scope, thus everything inside an if/else/for/while code block 
is the same as outside of it.

example:
def bar():
    my_variable = 9

    if 16 > 9:
        my_variable = 16

    print(my_variable)


bar()

Result will be 16. This won't be the case for other programming languages like java or c#. For example,

public class Main {
    public static void bar() {
        int myVariable = 9;

        if (16 > 9) {
            int myVariable = 16;  // ERROR: Already declared outside
        }

        System.out.println(myVariable); // Still prints 9
    }

    public static void main(String[] args) {
        bar();
    }
}
"""
import random

NUMLIST = list(range(1, 101))
#print(NUMLIST)
EASY = 10
HARD = 5

def check_guess(num, rand_num, attempts):
    if num != rand_num:
        attempts -= 1
        if num < rand_num:
            print("Too low.\n")
        elif num > rand_num:
            print("Too high.\n")
        return False, attempts
    else:
        return True, attempts

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
userDiff = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
rand_num = random.choice(NUMLIST)
#print(rand_num)

attempts = EASY if userDiff == "easy" else HARD
print(f"You have {attempts} attempts to guess the number.")
while attempts > 0:
    user_guess = int(input("\nMake a guess: "))
    result, attempts = check_guess(user_guess, rand_num, attempts)

    if result:
        print(f"You got it! The answer was {rand_num}.")
        break
    else:
        print(f"You have {attempts} attempts remaining to guess the number.")

if attempts == 0:
    print(f"Out of attempts! The correct number was {rand_num}.")