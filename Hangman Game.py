import random

# List of random words
word_list = [
    'python', 'algorithm', 'keyboard', 'internet', 'programming',
    'hangman', 'developer', 'function', 'variable', 'compile'
]

# Choose a random word
secret_word = random.choice(word_list)
revealed_letter = random.choice(secret_word)

# Initialize guessed word with revealed letter shown
guessed_word = [char if char == revealed_letter else '_' for char in secret_word]
guessed_letters = {revealed_letter}
max_attempts = 6
attempts_left = max_attempts

print("🎮 Welcome to Hangman!")
print(f"One letter has been revealed for you: '{revealed_letter}'")
print(f"You have {max_attempts} incorrect guesses allowed.")

# Game loop
while attempts_left > 0 and '_' in guessed_word:
    print("\nWord:", ' '.join(guessed_word))
    print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("⚠ You've already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in secret_word:
        print("✅ Correct!")
        for i, char in enumerate(secret_word):
            if char == guess:
                guessed_word[i] = guess
    else:
        attempts_left -= 1
        print(f"❌ Incorrect! Attempts left: {attempts_left}")

# Result
if '_' not in guessed_word:
    print(f"\n🎉 You won! The word was: {secret_word}")
else:
    print(f"\n💀 You lost! The word was: {secret_word}")