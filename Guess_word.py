import random
# Step 1: Generate a random word
word_list = ["python", "javascript", "java", "C++", "React"]
word = random.choice(word_list)
word_letters = list(word)
#print(word_letters)
# Step 2: Generate blanks
blanks = ["_"] * len(word)

# Step 3: Set lives
lives = random.randint(3, len(word_letters))

print("Welcome to the Word Guessing Game!")
print(" ".join(blanks))
print(blanks)
# Step 4: Game loop
while True:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter only!")
        continue
    # Step 5: Is the guessed letter in the word?
    if guess in word_letters:
        # Replace blanks with the letter
        for i, letter in enumerate(word_letters):
            if letter == guess:
                blanks[i] = guess
        print("Correct guess!")
    else:
        # Lose a life
        lives -= 1
        print(f"Wrong guess! You have {lives} lives left.")

    # Show current progress
    print(" ".join(blanks))

    # Step 6: Check win condition
    if "_" not in blanks:
        print("Congratulations! You guessed the word. Game over.")
        break

    # Step 7: Check lose condition
    if lives == 0:
        print(f"Out of lives! The word was '{word}'. Game over.")
        break