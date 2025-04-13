import tkinter as tk
import random
from Wordy import get_feedback, choose_random_word
import time

def load_words_from_file(file_path=r"C:\Users\hp\Desktop\Guipythonguess\word.txt"):
    word_dict = {}
    with open(file_path, "r") as file:
        for line in file:
            if ":" in line:
                word, category = line.strip().split(":", 1)
                word_dict[word.lower()] = category.lower()
    return word_dict
words = load_words_from_file()
def play_gui():
    difficulty_settings = {
        "Easy": {"length_range": (5,6), "max_attempts": 7, "hint_turn": 4},
        "Medium": {"length_range": (7,8), "max_attempts": 6, "hint_turn": 5},
        "Hard": {"length_range": (9,10), "max_attempts": 5, "hint_turn": None}
    }

    current_theme = {"mode": "light"}

    def apply_theme():
        bg = "#1e1e1e" if current_theme["mode"] == "dark" else "#f0f0f0"
        fg = "#ffffff" if current_theme["mode"] == "dark" else "#000000"
        root.configure(bg=bg)
        for widget in root.winfo_children():
            try:
                widget.configure(bg=bg, fg=fg)
            except:
                pass
        for frame in [start_frame, game_frame, guesses_frame, game_board]:
            for child in frame.winfo_children():
                try:
                    child.configure(bg=bg, fg=fg)
                except:
                    pass
        entry.configure(bg="#ffffff" if current_theme["mode"] == "light" else "#333333", fg=fg, insertbackground=fg)
        result_label.configure(bg=bg)

    def toggle_theme():
        current_theme["mode"] = "dark" if current_theme["mode"] == "light" else "light"
        apply_theme()

    target_word = ""
    category = ""
    MAX_ATTEMPTS = 8
    HINT_TURN = 4
    attempts = 0
    streak_counter = 0

    def start_game():
        nonlocal MAX_ATTEMPTS, HINT_TURN
        selected = difficulty_var.get()
        settings = difficulty_settings[selected]
        length_range = settings["length_range"]
        MAX_ATTEMPTS = settings["max_attempts"]
        HINT_TURN = settings["hint_turn"]
        start_frame.pack_forget()
        game_frame.pack()
        initialize_game(length_range, MAX_ATTEMPTS, HINT_TURN)

    def initialize_game(length_range, max_attempts, hint_turn, keep_streak=False):
        nonlocal target_word, category, attempts, streak_counter, MAX_ATTEMPTS, HINT_TURN
        MAX_ATTEMPTS = max_attempts
        HINT_TURN = hint_turn
        min_len, max_len = length_range
        attempts = 0
        if not keep_streak:
            streak_counter = 0
        streak_label.config(text=f"🔥 Current Streak: {streak_counter}")
        filtered = {w: c for w, c in words.items() if min_len <= len(w) <= max_len}
        if not filtered:
           feedback_label.config(text="No words found with that length_range!", fg="red")
           return
        target_word, category = choose_random_word(filtered)
        hint_title.config(text=f"Hint: It's a {category}.")
        entry.config(state="normal")
        submit_button.config(state="normal")
        entry.delete(0, tk.END)
        entry.focus_set()
        feedback_label.config(text=f"Guess a {min_len}-{max_len} letter word.", fg="blue")

        hint_label.config(text="")
        result_label.config(text="")
        new_game_button.config(state="disabled")
        for widget in guesses_frame.winfo_children():
            widget.destroy()
        apply_theme()


    def check_guess():
        nonlocal attempts, streak_counter
        guess = entry.get().strip().lower()
        if len(guess) != len(target_word):
            feedback_label.config(text=f"Enter a {len(target_word)}-letter word.", fg="red")
            return

        feedback = get_feedback(guess, target_word)
        display_guess_boxes(guess, feedback)

        if guess == target_word:
            result_label.config(text="🎉 You guessed it!", fg="green")
            streak_counter += 1
            disable_game()
            celebrate()
            new_game_button.config(state="normal")  
        else:
            if attempts + 1 == MAX_ATTEMPTS:
                result_label.config(text=f"❌ Game over! The word was '{target_word}'.", fg="red")
                disable_game()
                streak_counter = 0
                streak_label.config(text=f"🔥 Current Streak: {streak_counter}")

                game_over()
            elif HINT_TURN and attempts + 1 == HINT_TURN:
                hint = f"Hint: The word contains the letter '{random.choice(target_word)}'."
                hint_label.config(text=hint, fg="orange")
            shake_window()

        streak_label.config(text=f"🔥 Current Streak: {streak_counter}")
        attempts += 1
        entry.delete(0, tk.END)

    def disable_game():
        entry.config(state="disabled")
        submit_button.config(state="disabled")

    def restart_game():
        selected = difficulty_var.get()
        settings = difficulty_settings[selected]
        keep_streak = result_label.cget("text") == "🎉 You guessed it!"
        initialize_game(settings["length_range"], settings["max_attempts"], settings["hint_turn"], keep_streak=keep_streak)

        
    def display_guess_boxes(guess, feedback):
        row = tk.Frame(guesses_frame, bg=root["bg"])
        row.pack(pady=2)
        color_map = {"X": "#A9A9A9", "?": "#FFD700"}
        for i, char in enumerate(guess):
            color = "#32CD32" if feedback[i] == char else color_map.get(feedback[i], "#FF6347")
            box = tk.Label(row, text=char.upper(), bg=color, fg="white",
                           width=4, height=2, font=("Arial Rounded MT Bold", 14, "bold"),
                           relief="groove", borderwidth=2)
            box.pack(side="left", padx=2)

    def celebrate():
        result_label.config(text="🎉 You guessed it!", fg="green")
        emoji_burst(["🎉", "🎊", "✨", "🌟", "💥"])

    def emoji_burst(emojis, count=12):
        def animate(label, dx, dy, steps=10):
            def step(i=0):
                if i < steps:
                    label.place_configure(x=label.winfo_x() + dx, y=label.winfo_y() + dy)
                    root.after(50, lambda: step(i + 1))
                else:
                    label.destroy()
            step()

        for _ in range(count):
            emoji = random.choice(emojis)
            label = tk.Label(game_board, text=emoji, font=("Arial", 20), bg=game_board["bg"])
            x = random.randint(200, 400)
            y = random.randint(200, 300)
            dx = random.randint(-5, 5)
            dy = random.randint(-8, -2)
            label.place(x=x, y=y)
            animate(label, dx, dy)

        def pulse(count=0):
            if count > 6:
                result_label.config(bg=game_board["bg"])
                return
            color = "#ADFF2F" if count % 2 == 0 else "#32CD32"
            result_label.config(bg=color)
            root.after(200, lambda: pulse(count + 1))

        pulse()

    def game_over():
        shake_window()
    def shake_window():
        original_x = root.winfo_x()
        original_y = root.winfo_y()
        def shake(count=0):
            if count > 10:
                root.geometry(f"+{original_x}+{original_y}")
                return
            offset = random.randint(-10, 10)
            root.geometry(f"+{original_x + offset}+{original_y + offset}")
            root.after(30, lambda: shake(count + 1))
        shake()


    root = tk.Tk()
    root.title("Word Guessing Game")
    root.geometry("650x700")

    # Start frame
    start_frame = tk.Frame(root)
    start_frame.pack()

    tk.Label(start_frame, text="Select Difficulty", font=("Arial Rounded MT Bold", 18)).pack(pady=10)
    difficulty_var = tk.StringVar(value="Easy")
    for level in ["Easy", "Medium", "Hard"]:
        tk.Radiobutton(start_frame, text=level, variable=difficulty_var, value=level,
                       font=("Arial Rounded MT Bold", 14)).pack()
    tk.Button(start_frame, text="Start Game", command=start_game, font=("Arial Rounded MT Bold", 14)).pack(pady=10)

    theme_btn = tk.Button(root, text="🌙 Toggle Theme", command=toggle_theme, font=("Arial Rounded MT Bold", 12))
    theme_btn.pack(side="top", anchor="ne", padx=10, pady=10)

    game_frame = tk.Frame(root)

    game_board = tk.Frame(game_frame, bg="#e8f0fe", highlightbackground="#4a90e2",
                          highlightthickness=3, bd=15)
    game_board.pack(padx=20, pady=20, fill="both", expand=True)

    hint_title = tk.Label(game_board, text="", font=("Arial Rounded MT Bold", 18), bg="#e8f0fe")
    hint_title.pack(pady=10)

    tk.Label(game_board, text="Enter your guess:", font=("Arial Rounded MT Bold", 14), bg="#e8f0fe").pack()
    entry = tk.Entry(game_board, font=("Arial Rounded MT Bold", 18), width=20)
    entry.pack(pady=8)
    entry.bind("<Return>", lambda event: check_guess())

    submit_button = tk.Button(game_board, text="Submit", command=check_guess, font=("Arial Rounded MT Bold", 16))
    submit_button.pack(pady=8)

    feedback_label = tk.Label(game_board, text="", font=("Arial Rounded MT Bold", 14), bg="#e8f0fe")
    feedback_label.pack(pady=4)

    hint_label = tk.Label(game_board, text="", font=("Arial Rounded MT Bold", 14), fg="orange", bg="#e8f0fe")
    hint_label.pack()

    guesses_frame = tk.Frame(game_board, bg="#e8f0fe")
    guesses_frame.pack(pady=10)

    result_label = tk.Label(game_board, text="", font=("Arial Rounded MT Bold", 18), bg="#e8f0fe")
    result_label.pack(pady=10)

    streak_label = tk.Label(game_board, text=f"🔥 Current Streak:  {streak_counter}", font=("Arial Rounded MT Bold", 14), bg="#e8f0fe")
    streak_label.pack(pady=8)

    buttons_frame = tk.Frame(game_board, bg=game_board["bg"])
    buttons_frame.pack(pady=10)
    restart_button = tk.Button(buttons_frame, text="Restart Game", font=("Arial Rounded MT Bold", 14),
                           command=lambda: initialize_game(
                               difficulty_settings[difficulty_var.get()]["length_range"],
                               difficulty_settings[difficulty_var.get()]["max_attempts"],
                               difficulty_settings[difficulty_var.get()]["hint_turn"],
                               keep_streak=False))
    restart_button.pack(side="left", padx=10)

    new_game_button = tk.Button(buttons_frame, text="New Game", font=("Arial Rounded MT Bold", 14),
                            command=lambda: initialize_game(
                                difficulty_settings[difficulty_var.get()]["length_range"],
                                difficulty_settings[difficulty_var.get()]["max_attempts"],
                                difficulty_settings[difficulty_var.get()]["hint_turn"],
                                keep_streak=True))
    new_game_button.pack(side="left", padx=10)
    new_game_button.config(state="disabled")
    root.mainloop()

if __name__ == "__main__":

    play_gui()
