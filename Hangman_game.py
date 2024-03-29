import random
words = ['python', 'hangman', 'programming', 'computer', 'science', 'algorithm', 'software']
def choose_word(words):
    return random.choice(words)
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '-'
    return display
def reveal_letters(word):
    word_length = len(word)
    revealed_indices = random.sample(range(word_length), min(2, word_length))
    revealed_letters = [word[i] for i in revealed_indices]
    return revealed_letters
def hangman():
    word = choose_word(words)
    guessed_letters = []
    revealed_letters = reveal_letters(word)
    guessed_letters.extend(revealed_letters)
    attempts = 6  
    print("Welcome to Hangman!")
    print("Guess the word: ", display_word(word, guessed_letters))
    while True:
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        guessed_letters.append(guess)
        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if attempts == 0:
                print("You've run out of attempts. The word was:", word)
                break
        else:
            print("Good guess!")
        word_display = display_word(word, guessed_letters)
        print("Word: ", word_display)
        if '-' not in word_display:
            print("Congratulations! You've guessed the word:", word)
            break
hangman()