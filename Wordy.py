import os
import random
from termcolor import colored

# Core game logic
def get_feedback(guess, target):
    feedback = [""] * len(target)
    used_indices = set()
    for i in range(len(target)):
        if guess[i] == target[i]:
            feedback[i] = guess[i]
            used_indices.add(i)
    for i in range(len(target)):
        if feedback[i] == "":
            for j in range(len(target)):
                if j not in used_indices and guess[i] == target[j]:
                    feedback[i] = "?"
                    used_indices.add(j)
                    break
    for i in range(len(target)):
        if feedback[i] == "":
            feedback[i] = "X"
    return "".join(feedback)

def choose_random_word(words):
    return random.choice(list(words.items()))

# CLI version
try:
    import smartguesscli
except ImportError:
    print("Error: Could not import cli.py. Make sure it's in the same directory as this script.")
    exit(1)
    
# GUI version
try:
    import smartguessgui
except ImportError:
    print("Error: Could not import gui.py. Make sure it's in the same directory as this script.")
    exit(1)

# Main program
def main():
    print("Select the interface:")
    print("1. Command Line Interface (CLI)")
    print("2. Graphical User Interface (GUI)")

    choice = input("Enter your choice (1/2): ").strip()
    if choice == "1":
        smartguesscli.play_cli()
    elif choice == "2":
        smartguessgui.play_gui()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
