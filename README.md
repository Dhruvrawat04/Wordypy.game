# Wordypy: The Smart Guessing Game (with GUI and CLI)
Welcome to Wordypy, a word-guessing game where smart guesses lead you to victory!Wordypy uses advanced logic and a user-friendly graphical interface to make each guess smarter, bringing a unique twist to the traditional word-guessing format.

In Wordypy, your goal is to guess a randomly selected word within a set number of attempts, with feedback on every guess guiding your progress.

# Key Features
# Smart Guessing Mechanism:

The game ensures that each new guess is more refined based on the previous one, following these rules:

Eliminating Incorrect Letters: Letters that are not part of the target word will be excluded from future guesses.

Correct Placement: Letters in the correct position remain fixed in future guesses.

Wrong Position: Letters in the target word but in the wrong position are moved to new positions.

# Dynamic Difficulty Levels:

Choose between Easy, Medium, and Hard difficulty, which affect the word length, maximum attempts, and hint availability.

->Easy: 5–6 letter words, 7 attempts, hint on the 4th turn.

->Medium: 7–8 letter words, 6 attempts, hint on the 5th turn.

->Hard: 9–10 letter words, 5 attempts, no hint.

# Interactive Graphical Interface (GUI):

The game includes a fully interactive and visually appealing GUI built with Tkinter.

Users can toggle between light and dark themes for a personalized experience.

Streak tracking, animated feedback, and a celebration effect when you guess the word correctly.

An animated "shake" effect for incorrect guesses and game over situations.

# CLI (Command-Line Interface):

For users who prefer to play via the terminal, Wordypy also includes a command-line interface (CLI) to allow for a seamless guessing experience.

# Technologies Used
Python 3 for game logic.

Tkinter for the graphical user interface.

Python Tesseract library for optical character recognition (OCR), allowing the game to interpret word grids from images.

Random module to choose words and generate hints.

# How to Play 🚀
Choose Difficulty: Select from Easy, Medium, or Hard difficulty to set your preferred word length and number of attempts.

Guess the Word: Enter a guess, and receive feedback on each attempt.

->Green: Correct letter in the correct position.

->Yellow: Correct letter, wrong position.

->Red: Letter not in the word.

<>Hints: On certain difficulty levels, a hint will be provided to help you make the next guess.

<>Celebrate Victory: If you guess the word correctly, you win, and the game celebrates with an animated emoji burst.

<>Game Over: If you run out of attempts, the correct word is revealed, and the game resets.

Play Smart, Guess Smarter!
Start your journey with Wordypy and put your word-guessing skills to the test. Can you make the smartest guess and uncover the target word in fewer attempts?

# Game Modes 🌅🌃
Light and Dark Theme: The game includes a theme toggle, allowing players to switch between light and dark mode for the GUI.

Streak Tracker: Track your winning streak to see how many games in a row you've won.
