# Importing random module to use for shuffling the deck
import random

# Define a Card class
class Card:
    
    # Initialize the value and suit of the card when it is created
    def __init__(self, value, suit):
        self.value = value # Instance attribute associated with value of the card
        self.suit = suit   # Instance attribute associated with suit of the card

    # Define a string representation of the card
    def __str__(self):
        return f"{self.value} of {self.suit}"

# Define a Deck Class
class Deck:
    
    # Initialize the deck with 52 cards when it is created
    def __init__(self):
        self.cards = [] # Instance attribute associated with the deck of cards that is empty at the start
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']  # List of suits
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] # List of face values

        # Create a card for each combination of value and suit and add it to the deck
        for suit in suits: # Loop through each suit
            for value in values: # Loop through each value
                self.cards.append(Card(value, suit)) # Append the card to the deck

    # Implement the shuffle() operation
    def shuffle(self):
        # Implement the Fisher-Yates shuffle algorithm
        for card in range(len(self.cards)-1, 0, -1): # Loops from the last card to the first card
            rand_card = random.randint(0, card) # Picks a random card from the deck
            self.cards[card], self.cards[rand_card] = self.cards[rand_card], self.cards[card] # Swap the current card with the randomly selected card

# Implement the dealOneCard() operation
    def dealOneCard(self):
        if len(self.cards) == 0: # If the deck is empty
            print("Deck is empty") # Prints if there are no cards in deck
            return None # Returns None
        else:
            dealt_card = self.cards.pop() # Return the last card in the deck

        print("Card dealt: ", dealt_card) # Prints if a card is dealt
        print("Cards left in deck: ", len(self.cards)) # Prints the number of cards left in the deck
        
# Testing the shuffle and dealOneCard operations
deck = Deck() # Create a deck object
deck.shuffle() # Shuffle the deck of cards
for card in range(52): # Loop through each card in the deck
    deck.dealOneCard() # Deal one card from the deck
deck.dealOneCard() # Should return None since the deck is empty now