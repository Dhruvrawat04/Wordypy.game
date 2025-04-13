import random
from termcolor import colored
from Wordy import get_feedback, choose_random_word

def play_cli():
    def load_words_from_file(file_path=r"word.txt"):
        word_dict = {}
        with open(file_path, "r") as file:
            for line in file:
                if ":" in line:
                    word, category = line.strip().split(":", 1)
                    word_dict[word.lower()] = category.lower()
        return word_dict
    words = load_words_from_file()
    target_word, category = choose_random_word(words)
    MAX_ATTEMPTS = 8
    print(f"🎯 Guess the word! Hint: It's a {category}. The word has {len(target_word)} letters.\n")

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        guess = input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS}: ").strip().lower()

        if len(guess) != len(target_word):
            print(f"⚠️ Please enter a {len(target_word)}-letter word.\n")
            continue

        if guess == target_word:
            print(colored(f"🎉 Correct! The word was '{target_word}'. You got it in {attempts + 1} attempts!", "green"))
            return

        feedback = get_feedback(guess, target_word)
        print("Feedback:", colored_feedback(feedback))
        print("ℹ️  '?' = correct letter wrong position, 'X' = wrong letter.\n")

        if attempts == 3:
            print(colored(f"💡 Hint: The word contains the letter '{random.choice(target_word)}'.\n", "cyan"))

        attempts += 1

    print(colored(f"❌ Game over! The word was '{target_word}'. Better luck next time!", "red"))

def colored_feedback(feedback):
    styled = []
    for char in feedback:
        if char == "X":
            styled.append(colored(char, "red"))
        elif char == "?":
            styled.append(colored(char, "yellow"))
        else:
            styled.append(colored(char, "green"))
    return "".join(styled)
