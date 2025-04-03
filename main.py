# Import random module to use for shuffling the deck
import random

# Define a Card class to represent a playing card with a value and suit
class Card():
    
    # Cards need to have a value and a suit to be created
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit   

    # Provides a human-readable representation of the card
    def __str__(self):
        return f"{self.value} of {self.suit}"

# Define a Deck Class to represent a deck of 52 playing cards that can be shuffled and dealt
class Deck:
    
    # A deck of cards needs to be created with 52 cards
    def __init__(self):
        self.cards = [] # Stores all the cards in the deck
        self.build_deck() # Automatically build the deck when a Deck object is created
        self.current_index = 0 # Tracks the current index of the deck and the next card to be dealt

    # Populate the deck with 52 cards
    def build_deck(self):
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds'] 
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        print("Building deck...") 

        # Create a card for each combination of value and suit and add it to the deck
        for suit in suits: 
            for value in values: 
                self.cards.append(Card(value, suit)) 

    # Randomly shuffle the deck of cards using the Fisher-Yates shuffle algorithm
    def shuffle(self):
        print("Shuffling deck...")
        for card in range(len(self.cards)-1, 0, -1): # Iterate through the deck in reverse order
            rand_card = random.randint(0, card) # Get a random index from 0 to the current card index
            self.cards[card], self.cards[rand_card] = self.cards[rand_card], self.cards[card] # Swap the current card with the random card
            self.current_index = 0 # Reset dealing index to 0 after shuffling for a fresh start
        print("Deck shuffled!") 

    # Retrieve the next card from the deck and check to see if the deck is empty
    def dealOneCard(self):
        if self.current_index >= len(self.cards): # To ensure that we don't deal more cards than available in the deck
            print("No card dealt, deck is empty!")
            return None 
        else: 
            dealt_card = self.cards[self.current_index] # Get the next card from the deck
            self.current_index += 1 # Increment the current index for next deal
            print("Card dealt: ", dealt_card) 
            return dealt_card 
    
    # Determine the number of cards left in the deck
    def cards_left(self):
        return len(self.cards) - self.current_index

deck = Deck() # Create a deck object
deck.shuffle() # Shuffle the deck of cards before dealing

# Deal 52 cards from the deck
for card in range(52): 
    deck.dealOneCard()

print("Cards left in deck: ", deck.cards_left()) # Confirm that the deck is empty after dealing all cards

deck.dealOneCard() # Attempt to deal one more card from the deck after all cards have been dealt
