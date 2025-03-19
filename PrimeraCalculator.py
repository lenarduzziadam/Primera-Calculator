import sys
from tkinter import Canvas, Label, BOTH
import tkinter as tk




#Dictionary of primera values for each card
PRIMERA_VALUES = {
    7: 21, #value of rank 7 is 21 
    6: 18, #value of rank 6 is 18
    1: 16,
    5: 15,
    4: 14,
    3: 13,
    2: 12,
    
    10: 10, #value of rank 10-8 is 10
    9: 10,
    8: 10
    
}

SUITS = ["coins", "cups", "swords", "clubs"]

def print_primera_rules():
    print("\n=== PRIMIERA SCORING RULES ===")
    print("In Primiera scoring, cards have special point values:")
    print("  7 = 21 points (highest)")
    print("  6 = 18 points")
    print("  1 (Ace) = 16 points")
    print("  5 = 15 points")
    print("  4 = 14 points")
    print("  3 = 13 points")
    print("  2 = 12 points")
    print("  Face cards (8, 9, 10) = 10 points each (lowest)")
    print("\nYour Primiera score is calculated by:")
    print("1. Taking your highest card in each suit")
    print("2. Adding those four values together")
    print("3. The maximum possible score is 84 (all four 7s)")
    print("=====================================\n")
def calculate_primera_score():
    total = 0
    for suit in SUITS:
        print(f"What is highest primera card rank in {suit} Suit")
        rank_input = input("input best rank here: \n")
        
        if int(rank_input) == 0:
            print(f"Aww too bad you didn't recieve any {suit} cards")
            total += 0
        else:
            if int(rank_input) is None or not isinstance(int(rank_input), int) or int(rank_input) not in PRIMERA_VALUES:
                raise ValueError("Not valid type")
            if int(rank_input) > 10 or int(rank_input) < 0:
                raise Exception("not a valid rank in Scopa deck")
            else:
                print(f"congrats looks like you have recieved {PRIMERA_VALUES[int(rank_input)]} points today")
                total += PRIMERA_VALUES[int(rank_input)]
    print(f"You have a grand total of {total} points congrats Nino")
    return
            
            
class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        #sets root widget title
        self.root = tk.Tk()
        self.root.title("Primera Calculator")
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        
        #create canvas with root keeping width and height as parameters
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        
        #creates label widget
        self.label = tk.Label(self.root, text="In Primiera scoring, cards have special point values:")
        self.label.pack()
        
        self.create_entry()
        
        self.running = False
    
    def create_entry(self):
        # creating a entry for input
        # name using widget Entry
        num_var=tk.StringVar()
        num=num_var.get()
        num_entry = tk.Entry(self.root,textvariable = num_var, font=('calibre',10,'normal'))
        score = 0
        score += PRIMERA_VALUES[int(num)]
    
    
    #closing method
    def close(self):
        #sets running variable to False
        self.running = False