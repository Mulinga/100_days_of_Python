import random
from hangman_words import word_list
from hangman_art import hangman_stages, hangman_logo

lives = 6
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
guessed_letters = []

# Print the logo (fix: it's a string, not a list)
print(hangman_logo)

print("======== Welcome to Hangman! =========")
print(f"The magic word is: {'_ ' * word_length}".strip())

game_over = False

while not game_over:
    guess = input("\nGo on and guess a letter:\n").lower()

    if guess in guessed_letters:
        print(f"You've already guessed letter {guess}.")
        continue

    guessed_letters.append(guess)

    # Display the current state of the word
    display = ""
    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print(f"\n{display.strip()}")

    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry! You guessed {guess}. Which is not in the magic word!")
        if lives > 0:
            print(f"You have {lives} {'life' if lives == 1 else 'lives'} left.")
        if lives == 0:
            game_over = True
            print("\n============= Sorry. You Lost! ============")
            print(f"The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("\n============== You Won!! ==============")

    print(hangman_stages[lives])
