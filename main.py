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


# Testing the Card class
card = Card('Ace', 'Hearts') # Create a card object
print(card) # Print the value and suit of the card

# Implement the shuffle() operation
    # Must return no value
    # Results in cards in the deck being randomly permuted
    # Do NOT use the library-provided shuffle function
    # Do use the library-provided random number generator

# Implement the dealOneCard() operation
    # Returns one card from the deck to the caller
    # A call to shuffle mused be followed by 52 calls to dealOneCard()
    # this should result in the caller being provided all 52 cards of the deck in a random order
    # if the caller makes a 53rd call to dealOneCard(), the caller should receive None

# Must implement the principle of least surprise

# Add security checks to ensure that the code meets the requirements for Appian's security standards