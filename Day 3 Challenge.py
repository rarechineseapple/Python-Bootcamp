import random
import time

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

signs = [] # intialize a new signs list
signs.extend([rock, paper, scissors]) # option one
#signs += [rock, paper, scissors] # option two, works the same as above
#option three, append three times

gameon = True

while True:

    #Below is the code for the actual game
    #pc_decision = random.randint(0,2)
    #print(signs[pc_decision]) for testing

    rps = input("Rock Paper Scissors. Type 0 for Rock, 1 for Paper, 2 for Scissors.\n")

    # if rps.lower() == "q": # check if user wants to quit
    #     print("Thanks for playing.")
    #     break
    # if not rps.isdigit():
    #     print("Invalid input!")
    #
    # rps = int(rps) # convert user input into int
    #
    # if rps not in range(3):
    #     print("Invalid choice! Only enter 0, 1 or 2.\n")
    #     continue
    #
    # print(f"\nYou chose: \n {signs[rps]}")
    # print(f"\nComputer chose: \n {signs[pc_decision]}")
    #
    # if rps == pc_decision:
    #     print("It's a tie!")
    # elif (rps == 0 and pc_decision == 1) or (rps == 2 and pc_decision == 0) or (rps == 1 and pc_decision == 2):
    #     print("You lose!")
    # else:
    #     print("You win!")

    #Computer cheating version
    if rps.lower() == "q": # check if user wants to quit
        print("Thanks for playing.")
        break
    if not rps.isdigit():
        print("Invalid input!")

    rps = int(rps) # convert user input into int

    if rps not in range(3):
        print("Invalid choice! Only enter 0, 1 or 2.\n")
        continue


    pc_decision = (rps + 1) % 3  # computer picks the winning move

    print(f"\nYou chose: \n {signs[rps]}")
    print(f"\nComputer chose: \n {signs[pc_decision]}")

    print("You lose! Press q to quit.")


    # #Works but poor example
    # if rps == pc_decision:
    #     print("It's a tie!")
    #
    # elif rps == 0 and pc_decision == 1:
    #     print("You lose")
    # elif rps == 1 and pc_decision == 0:
    #     print("You win")
    #
    # elif rps == 0 and pc_decision == 2:
    #     print("You win")
    # elif rps == 2 and pc_decision == 0:
    #     print("You lose")
    #
    # elif rps == 1 and pc_decision == 2:
    #     print("You lose")
    # elif rps == 2 and pc_decision == 1:
    #     print("You win")
    #
    # else:
    #     print("wrong input")


