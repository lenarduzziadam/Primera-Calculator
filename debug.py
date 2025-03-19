import sys
from tkinter import *

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

# Create an entry widget
entry = Entry(window, width=30)
entry.pack(pady=10)


window.mainloop()
