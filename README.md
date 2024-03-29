**Hangman Game**

This is a simple Hangman game implemented in Python.

### How to Play

1. Run the Python script.
2. The game will choose a random word from a predefined list.
3. You will be prompted to guess letters to reveal the word.
4. You have 6 attempts to guess the word correctly.
5. If you guess a letter correctly, it will be revealed in the word.
6. If you guess a wrong letter, you will lose an attempt.
7. Keep guessing letters until you either reveal the word or run out of attempts.

### Game Rules

- You can only enter one letter at a time.
- Letters are case insensitive.
- You cannot guess the same letter twice.

### Code Explanation

- The `choose_word` function selects a random word from a predefined list of words.
- The `display_word` function displays the current state of the word, showing guessed letters and dashes for unrevealed letters.
- The `reveal_letters` function reveals a few random letters in the word at the start of the game.
- The `hangman` function implements the game logic, including prompting for user input, checking guesses, and handling game over conditions.

Enjoy playing Hangman!
