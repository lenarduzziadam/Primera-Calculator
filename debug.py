import sys
from tkinter import *
from tkinter import messagebox
from PrimeraCalculator import *

window = Tk()
window.geometry("400x500")
window.resizable(True, True)
window.title("Primera Calculator")

instruction_text = """=== PRIMIERA SCORING RULES ===
In Primiera scoring, cards have special point values:
  7 = 21 points (highest)
  6 = 18 points
  1 (Ace) = 16 points
  5 = 15 points
  4 = 14 points
  3 = 13 points
  2 = 12 points
  Face cards (8, 9, 10) = 10 points each (lowest)

Your Primiera score is calculated by:
1. Taking your highest card in each suit
2. Adding those four values together
3. The maximum possible score is 84 (all four 7s)
====================================="""

label = Label(window,text=instruction_text)
label.pack()

def check_entry():
    #creates entry for user inpuut
    user_input = entry.get()
    if int(user_input) in PRIMERA_VALUES:
        result = f"'{int(user_input)}' found: {PRIMERA_VALUES[int(user_input)]}"
    else:
        result = f"'{user_input}' not found in dictionary."
    messagebox.showinfo("Result", result)
    
def calculate_primera_score_tk():
    total = 0
    for suit in SUITS:
        first = Label(window, text=f"What is highest primera card rank in {suit} Suit")
        first.pack()
        
        rank_input = calculator.get()
        
        # Check if input is empty
        if not rank_input:
            error = Label(window, text=f"Please enter a value for {suit} suit")
            error.pack()
            continue
        
        # Check if input is "0"
        if rank_input == "0":
            error = Label(window, text=f"Aww too bad you didn't receive any {suit} cards")
            error.pack()
            total += 0
            continue
        
        # Try to convert to integer and validate
        try:
            rank_input_int = int(rank_input)
            if rank_input_int < 0 or rank_input_int > 10:
                error = Label(window, text=f"Not a valid rank in Scopa deck (must be 0-10)")
                error.pack()
                continue
            else:
                congrats = Label(window, text=f"Congrats! You have received {PRIMERA_VALUES[rank_input_int]} points")
                congrats.pack()
                total += PRIMERA_VALUES[rank_input_int]
        except ValueError:
            error = Label(window, text=f"Please enter a valid number for {suit} suit")
            error.pack()
            continue
    
    finished = Label(window, text=f"You have a grand total of {total} points. Congrats Nino!")
    finished.pack()
    return

# Create an entry widget
entry = Entry(window, width=30)
calculator = Entry(window, width=42)
entry.pack(pady=10)

check_button = Button(window, text="Enter Value", command=calculate_primera_score_tk())
check_button.pack(pady=10)

window.mainloop()
