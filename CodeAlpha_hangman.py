import random

words = ["apple", "tiger", "python", "school", "computer"]

word = random.choice(words)
guessed = []
attempts = 6

print("Welcome to Hangman Game!")

while attempts > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Attempts left:", attempts)

    if all(letter in guessed for letter in word):
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
    elif guess in guessed:
        print("You already guessed that letter.")
    else:
        guessed.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

else:
    print("Game Over!")
    print("The word was:", word)