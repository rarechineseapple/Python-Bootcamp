import threading
import time
from random import choice


# function to handle the countdown timer
# TimerThread class inherits from threading.Thread to allow the class to run in a separate thread, so countdown timer can run in parallel with the game.
# Why we use threading is because we want to allow user input during the countdown.
#for events that do not require user input we can simply use timer.sleep()
class TimerThread(threading.Thread):
    def __init__(self, time_limit): # constructor method which initializes the object and time_limit is the parameter representing number of seconds.
        super().__init__() # calls constructor of parent class threading.thread to initialize the thread.
        self.time_limit = time_limit # original time limit
        self.time_remaining = time_limit # stores time remaining
        self.timer_stopped = False # boolean flag

    # method defining the main behavior of timer
    def run(self):
        while self.time_remaining > 0 and not self.timer_stopped:
            time.sleep(1)
            self.time_remaining -= 1
        if self.time_remaining == 0 and not self.force_stop_message:
            print("\nTime's up!")
            self.timer_stopped = True

    # stop countdown, signal to run() method that timer should stop when player respond before time runs out
    def stop(self):
        self.timer_stopped = True

# function to prompt for user input with a time limit
def timeout(prompt, time_limit):
    print(prompt, end=" ", flush=True)
    timer = TimerThread(time_limit)
    timer.start()

    # wait for user input within the time limit
    user_input = input()
    timer.stop()  # stop timer
    timer.join()  # ensure timer thread finishes
    if user_input == "":  # timeout case if input is empty
        return "timeout"
    return user_input.lower()


print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("\nWelcome to Treasure Island, where the winds whisper tales of a long-lost fortune waiting to be claimed.\n"
      "You, an adventurous soul seeking the thrill of discovery, have just arrived at the mysterious island.\n"
      "But beware, danger lurks at every corner, and only the wisest choices will lead you to treasure.\n"
      "Will you emerge victorious, or will you fall victim to the island's many perils?\n"
      "The fate of your adventure is in your hands.\n")

direction = str(input("Choose a direction. Left, or Right? ")).lower()

if direction == "left":
    print(r'''          
                    ... ....                     .. ...                           ____,--
              .. ...... .                           ........__                  __,'MMII;:.
            ...                                      ......|__|            _,--'MMI;:.
                                                @         /|. .          ,'MMI;:.WI;;:.
                        ,d888b,                |.\       / |\           /MWI;;  WWI;.
                       J8888888L               |' \     /^^|^\        ,'MWI;   WWWI;;:.
                       888888888               |. o\ __/___|__\_   ,-'MWI;:.  WI;;::.
            -----------------------------------|.  L\-`--------'--'_MWI;:.   WWI;;:.
                  - -__--__--__--__ -           \.   \                `---. WI;:.     ____-
                   - __--__--__-- _             |:    :.                   `/|-------'
                    _ -__--__--_ -              |:     ::.                ,''/
                      - _--__- _                |/       ::.             /: |
            ___        _ --__ -                 /'         :`--.______,-::  /
            ###\        _ -_ -                 /'   ._ .     ``        '    `-_
            ,--'         --__              _,-'   __/. .... .  .  ___,---.__,-'-.
                          -_         __,--/'   __/##`-._____,----'::::::::::::::#\
                                          `---'`````##:::::::::::::::::::::::::::#`---.
                                                   `````::::::::::::#######:::####\'''')

    print("\nYou come across a lake. There is an island in the middle of the lake. Probably the treasure island.\n Do you wish to wait for a boat, or swim across?")
    lake = str(input("Wait or Swim? \n")).lower()
    if lake != "wait":
        print("\nYou got attacked and swallowed up by sharks! Game Over.")
    else:
        print("\nAfter a few moments, a small boat drifts toward you, its oars cutting through the water with rhythmic precision.\n"
              "A grizzled old man in a weathered coat gestures for you to hop in.\n"
              "Climb aboard, he says with a nod. 'This island won't reach itself.'\n")
        print("You arrived at the island unharmed. You see a cave and head inside to find that there are three different paths.\n")

        path1_open = True

        while True:
            path = str(input("Choose path 1, 2, or 3: "))
            if path == "1" and path1_open:
                print("You enter the first path. The cave is wretchedly cold and grim.")
                time.sleep(2)
                print("You notice a pair of glowing eyes peering at you from the shadows.")
                time.sleep(2)
                print(r'''                                              
                                                        ,--,  ,.-.
                            ,                   \,       '-,-`,'-.' | ._
                           /|           \    ,   |\         }  )/  / `-,',
                           [ '          |\  /|   | |        /  \|  |/`  ,`
                           | |       ,.`  `,` `, | |  _,...(   (      _',
               -ART BY-    \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                -ZEUS-      \  \_\,``,   ` , ,  /  |         )         _,/
                             \  '  `  ,_ _`_,-,<._.<        /         /
                              ', `>.,`  `  `   ,., |_      |         /
                                \/`  `,   `   ,`  | /__,.-`    _,   `\
                            -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                             \_,,.) /\    ` /  / ) (-,, ``    ,        |
                            ,` )  | \_\       '-`  |  `(               \
                           /  /```(   , --, ,' \   |`<`    ,            |
                          /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                    ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
                   (-, \           ) \ ('_.-._)/ /,`    /
                   | /  `          `/ \\ V   V, /`     /
                ,--\(        ,     <_/`\\     ||      /
               (   ,``-     \/|         \-A.A-`|     /
              ,>,_ )_,..(    )\          -,,_-`  _--`
             (_ \|`   _,/_  /  \_            ,--`
              \( `   <.,../`     `-.._   _,-`
               `                      ```
               ''')
                print("HOLY MOLY ITS A MONSTER!\n")
                run = timeout("\nAre you gonna run? Yes or No? ", 6).lower()

                if run == "yes" or run == "y":
                    print("\nYOU SURVIVE!\nAs you dash out of that cave entrance,a large mass of rocks collapses and blocks off the entrance to this path.\n")
                    path1_open = False
                    continue

                else:
                    if run == "timeout":
                        print("\nThe monster catches you. You died! Game Over!")
                        break
                    else:
                        print("\nThe monster ripped you in half! You died! Game Over!")
                        break

            elif path == "2":
                print(r'''
                        (
                       (_)
                       ###
                       (#c     _\|/_
                        #\     wWWWw
                        \ \-. (/. .\)
                        /\ /`\/\   /\
                        |\/   \_) (_|
                        `\.' ; ;    ;`\
                          `\;  ;    .  ;/\
                            `\;    ;  ;|  \
                             ;   .' '  ;  /
                             |_.'   ;  | /)
                             (     ''._;'`
                             |    ' . ;
                             |.-'   .:)
                             |        |
                             (  .'  : |
                             |,-  .:: |
                             | ,-'  .;|
                         jgs_/___,_.:_\_
                           [I_I_I_I_I_I_]
                           |I_I_I_I_I_I_|
                        _|=--------------=|_
                ''')
                print("As you step into the final chamber, your breath catches in your throat.\n"
                      "The cavern shimmers with golden light, reflecting off a small, jeweled idol perched atop an ancient pedestal.\n"
                      "Gold coins, gemstones, and treasures beyond measure spill around it in gleaming piles.\n"
                      "It’s a king’s ransom, enough to live in luxury forever.\n")
                choice = str(input("Do you pick it up? ")).lower()

                if choice == "yes" or choice == "y":
                    print("The moment your fingers close around the golden idol, the cavern rumbles.\n"
                          "The walls tremble, and suddenly-\n")
                    time.sleep(2)
                    print("Gold begins falling from the ceiling.\n"
                          "A handful at first, then a torrent. It's incredible, more treasure than you could have imagined!\n")
                    time.sleep(2)
                    print("But then, the coins don't stop.\n"
                          "They fall faster. Heavier. The room is filling up, and soon, you're sinking under the weight of endless riches.\n")
                    choice2 = str(input("Drop the idol? (Y/N)")).lower()

                    if choice2 == "yes" or choice2 == "y":
                        print("\nThe moment you let go, the gold stops falling, and the piles shift away like a retreating tide.\n"
                        "The idol clatters to the floor, untouched once more. You escape from the island—but leave empty-handed.\n")
                        time.sleep(2)
                        print("Game Over!")
                        break
                    elif choice2 == "no" or choice2 == "n":
                        print("\nThe gold keeps falling, burying you in an avalanche of your own greed.\n")
                        time.sleep(2)
                        print("Game Over!")
                        break
                    else:
                        print("Invalid input, please retry.")

                elif choice == "no" or choice == "n":
                    print("\nYou leave the idol where it is and head back out.\n")
                    continue

                else:
                    print("invalid input, please retry.")


            elif path == "3":
                print(r"""  
                            o
                               O       /`-.__
                                      /  \�'^|
                         o           T    l  *
                                    _|-..-|_
                             O    (^ '----' `)
                                   `\-....-/^
                         O       o  ) "/ " (
                                   _( (-)  )_
                               O  /\ )    (  /\
                                 /  \(    ) |  \
                             o  o    \)  ( /    \
                               /     |(  )|      \
                              /    o \ \( /       \
                        __.--'   O    \_ /   .._   \
                       //|)\      ,   (_)   /(((\^)'\
                          |       | O         )  `  |
                          |      / o___      /      /
                         /  _.-''^^__O_^^''-._     /
                       .'  /  -''^^    ^^''-  \--'^
                     .'   .`.  `'''----'''^  .`. \
                   .'    /   `'--..____..--'^   \ \
                  /  _.-/                        \ \
              .::'_/^   |                        |  `.
                     .-'|                        |    `-.
               _.--'`   \                        /       `-.
              /          \                      /           `-._
              `'---..__   `.                  .�_.._   __       \
                       ``'''`.              .'gnv   `'^  `''---'^
                              `-..______..-
                        """)
                print("You step into the dimly lit chamber, you’re met by a figure cloaked in tattered robes.\n"
                      "Before you stands a wizened old wizard, his eyes gleaming with a mysterious intensity.\n"
                      "You seek the treasure, do you? he says, his voice echoing softly around the room. But first, you must prove your wit.\n"
                      "Answer me this riddle correctly, and the treasure is yours. Fail, and you will be banished.\n"
                      "The wizard leans forward slightly, he raises his hand, and with a flick of his fingers, the room grows colder.\n")

                riddle = str(input("\nWhat word is spelled incorrectly in every dictionary? ")).lower()
                if riddle == "incorrectly":
                    print("\nThe moment you answer correctly, the wizard nods approvingly. \nHis eyes twinkle with a knowing smile."
                    "Impressive, he says, his voice softer now. You have answered wisely. The treasure is yours.\n"
                    "With a snap of his fingers, the ground beneath you trembles, and a chest slowly rises from the floor, golden and ancient.\n"
                    "The wizard steps aside, allowing you to claim your prize. Go forth, he says with a whisper. You have earned it.")

                    # 5 second delay for dramatic effect
                    time.sleep(5)

                    print("\n\n\n\n\n")
                    print(r"""                 
                                            _.--.
                                        _.-'_:-'||
                                    _.-'_.-::::'||
                               _.-:'_.-::::::'  ||
                             .'`-.-:::::::'     ||
                            /.'`;|:::::::'      ||_
                           ||   ||::::::'     _.;._'-._
                           ||   ||:::::'  _.-!oo @.!-._'-.
                           \'.  ||:::::.-!()oo @!()@.-'_.|
                            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
                              `>'-.!@%()@'@_%-'_.-o _.|'||
                               ||-._'-.@.-'_.-' _.-o  |'||
                               ||=[ '-._.-\U/.-'    o |'||
                               || '-.]=|| |'|      o  |'||
                               ||      || |'|        _| ';
                               ||      || |'|    _.-'_.-'
                               |'-._   || |'|_.-'_.-'
                            jgs '-._'-.|| |' `_.-'
                                    '-.||_/.-'
                                    
                        Congratulations! You have won the game!
                    """)
                    break

                else:
                    print("\nThe wizard's eyes darkens as your answer falls short. \nWith a sigh, he shakes his head. 'A shame. The treasure"
                          " was not meant for you.' \nThe room begins to swirl around you, the walls closing in as if the very stones themselves reject your presence.\n"
                          "The wizard raises his hands and a gust of wind sends you flying off the island.\nGAME OVER!")
                    break

            elif path == "1" and not path1_open:
                print("There is a large mass of rocks blocking the entrance to this path. Choose another path.\n")

            else:
                print("Invalid input, please retry.")

else:
    print("You fell into a hole! Game Over.")





