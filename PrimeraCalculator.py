import sys

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

def calculate_primera_scor(captured_cards):
    
    #initiates best value for each suit to 0
    best_by_suit = {suit: 0 for suit in SUITS} 
    
    #for each captured cards checks if its the highest in the suit (iterates through  rank ano)
    for rank, suit in captured_cards:
        value = PRIMERA_VALUES.get(rank, 0) # sets tuple suit value to zero, and completes tuple (rank, suit) for primera  getting the primera value for the rank
        
        #if value has a better value than the current best by suit update best by suit to value. 
        if value > best_by_suit[suit]:
            best_by_suit[suit] = value
            
    #calculates overall score via adding best value of each suit
    total_score = sum(best_by_suit.values())
    
    return total_score, best_by_suit

def get_user_cards():
    cards = []
    print("enter captured cards")
    print("Format: [rank] of [suit]")
    print("type d when finished")
    
    while True:
        card_input = input("> ").strip().lower()
        if card_input == 'd':
            break
        split = card_input.split("of")
        card_rank = split[0]
        card_suit = split[1]
        if card_rank in PRIMERA_VALUES and card_suit in PRIMERA_VALUES:
            cards.append((card_rank, card_suit,)) 
        else:
            raise Exception("invalid card and/or rank try again")
        # TODO: Implement parsing the card input
        # Hint: Split the input by 'of' and extract the rank and suit
        # Make sure to validate the input (valid rank and suit)
        # If valid, add (rank, suit) tuple to cards list
        # If invalid, print an error message and continue
        
   
   
   
   
    return cards