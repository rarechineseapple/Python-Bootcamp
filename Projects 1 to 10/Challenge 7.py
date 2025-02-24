import random
import hangman_words as hw
import hangman_art as ha

chosen_word  = random.choice(hw.word_list).lower()
#print(chosen_word)

lives = 6

blanks = ["_"] * len(chosen_word)

game_over = False
print(ha.logo)
print(ha.stages[6])

guessed_letters = set()

# game runnning
while not game_over:

    user_guess = input("\nGuess a letter: ").lower()

    # prevent any inputs that is not a single letter
    if not user_guess.isalpha() or len(user_guess) != 1:
        print("Invalid input! Please enter a single letter.\n")
        continue

    # prevent re-guessing of same correct* letter
    if user_guess in guessed_letters:
        print("You've already guessed that letter!\n")
        continue

    guessed_letters.add(user_guess)

    if user_guess in chosen_word:
        print(f"Good guess! {user_guess} is indeed in the word.\n")
        for i in range(len(chosen_word)):
            if chosen_word[i] == user_guess:
                blanks[i] = user_guess

    else:
        lives -= 1
        print(ha.stages[lives])
        print(f"Wrong! You have {lives} lives left.\n")

    print(" ".join(blanks))

    # check win cons after each turn

    if "_" not in blanks:
        game_over = True
        print("YOU WIN!")

    elif lives == 0:
        game_over = True
        print(f"\nThe gallows claim another soul... Better luck next time.")
        print(f"\nThe word was {chosen_word}.")
        print("YOU LOSE!")