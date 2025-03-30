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

    # Define a string representation of each card in the deck
    # def __str__(self):
        # return ", ".join(str(card) for card in self.cards) 
    
    # Implement the shuffle() operation
    def shuffle(self):
        # Implement the Fisher-Yates shuffle algorithm
        for card in range(len(self.cards)-1, 0, -1): # Loops from the last card to the first card
            rand_card = random.randint(0, card) # Picks a random card from the deck
            self.cards[card], self.cards[rand_card] = self.cards[rand_card], self.cards[card] # Swap the current card with the randomly selected card

        # Testing the shuffle operation
        print("Shuffled deck:")
        print(", ".join(str(card) for card in self.cards))
    
    # Must return no value
    # Results in cards in the deck being randomly permuted
    # Do NOT use the library-provided shuffle function
    # Do use the library-provided random number generator

# Testing the Deck class
deck = Deck() # Create a deck object
deck.shuffle() # Shuffle the deck of cards

# Testing the Card class
# card = Card('Ace', 'Hearts') # Create a card object
# print(card) # Print the value and suit of the card
# print(len(deck.cards)) # Print the number of cards in the deck (should be 52)
# print(deck.cards[0]) # Print the first card in the deck
# print(deck.cards[51]) # Print the last card in the deck
# print(deck) # Print the entire deck of cards, each split by a comma


# Implement the dealOneCard() operation
    # Returns one card from the deck to the caller
    # A call to shuffle mused be followed by 52 calls to dealOneCard()
    # this should result in the caller being provided all 52 cards of the deck in a random order
    # if the caller makes a 53rd call to dealOneCard(), the caller should receive None

# Must implement the principle of least surprise

# Add security checks to ensure that the code meets the requirements for Appian's security standards