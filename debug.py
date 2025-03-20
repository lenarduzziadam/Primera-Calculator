import sys
from tkinter import *
from tkinter import messagebox, font
from PrimeraCalculator import *

window = Tk()
window.geometry("1000x1500")
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
custom_font = font.Font(family="Comic Sans MS", size=22)
label = Label(window,text=instruction_text, font=custom_font)
label.pack()

def check_entry():
    #creates entry for user inpuut
    total = 0
    user_input = entry.get()
    input_2 = calculator.get()
    input_3 = coins.get()
    input_4 = clubs.get()
    if int(user_input) in PRIMERA_VALUES:
        total += PRIMERA_VALUES[int(user_input)]
        if int(input_2) in PRIMERA_VALUES and int(input_3) in PRIMERA_VALUES and int(input_4) in PRIMERA_VALUES:
            total += PRIMERA_VALUES[int(input_2)]
            total += PRIMERA_VALUES[int(input_3)]
            total += PRIMERA_VALUES[int(input_4)]
            
            in_label = Label(window, text=f"Grand Total: {total}", font=custom_font)
            in_label.pack()
        
        result = f"Grand TOTAL: {total}"
    else:
        result = f"'{user_input}' not found in dictionary."
    messagebox.showinfo("Result", result)
    

# Create an entry widget
entry = Entry(window, width=30, text="CUPS")
calculator = Entry(window, width=30)
coins = Entry(window, width=30)
clubs = Entry(window, width=30)
entry.pack()
calculator.pack()
coins.pack()
clubs.pack()


cups_button = Button(window, text="Enter Values", command=check_entry)

cups_button.pack(pady=10)

window.mainloop()
