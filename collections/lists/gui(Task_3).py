import tkinter as tk
from tkinter import messagebox

# Define the original word and scrambled word
original_word = "recommendation"
scrambled_word = "eoommandretnic"

# Create the hint slices
hint1_slice = original_word[4:6] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"
hint2_slice = original_word[-3:] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"
hint3_slice = original_word[7:10] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"
hint4_slice = original_word[:2] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"

# Function to check if the user's guess is correct
def check_guess():
    guess = entry_guess.get().lower()
    if guess == original_word:
        messagebox.showinfo("Congratulations!", "You guessed the word correctly!")
    else:
        messagebox.showerror("Incorrect Guess", "Sorry, that's not the correct word. Try again.")

# Create a Tkinter window
window = tk.Tk()
window.title("Word Guessing Game")

# Display game instructions and hints
label_scrambled_word = tk.Label(window, text="Scrambled word: " + scrambled_word)
label_scrambled_word.pack()

label_instructions = tk.Label(window, text="Guess the original word from the scrambled version.")
label_instructions.pack()

label_hint1 = tk.Label(window, text="Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")
label_hint1.pack()

label_hint2 = tk.Label(window, text="Hint 2: The last 3 letters are '" + hint2_slice + "'.")
label_hint2.pack()

label_hint3 = tk.Label(window, text="Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")
label_hint3.pack()

label_hint4 = tk.Label(window, text="Hint 4: The first two letters are '" + hint4_slice + "'.")
label_hint4.pack()

# Entry field for user's guess
entry_guess = tk.Entry(window)
entry_guess.pack()

# Button to submit guess
button_submit = tk.Button(window, text="Submit Guess", command=check_guess)
button_submit.pack()

# Run the Tkinter event loop
window.mainloop()