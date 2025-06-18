import random

# List of words
words = ['python', 'hangman', 'codealpha', 'intern', 'project','game','weeks']
word = random.choice(words)

# Setup
hidden_word = ['_'] * len(word)
guessed = []
lives = 6

print("Welcome to Hangman!")
print("Guess the word. You have 6 wrong attempts.\n")

while lives > 0 and '_' in hidden_word:
    print("Word:", ' '.join(hidden_word))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Enter one valid letter.\n")
        continue

    if guess in guessed:
        print("You already guessed that letter.\n")
        continue

    guessed.append(guess)

    if guess in word:
        print(" Nice!\n")
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        lives -= 1
        print(f" Wrong! Lives left: {lives}\n")

# Final result
if '_' not in hidden_word:
    print(" You won! Word was:", word)
else:
    print("You lost! Word was:", word)
