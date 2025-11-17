# AadenGabrielAbarintos_ProgrammingExercise_11.py
# This program deals a Poker hand of five cards.
# Then the program prompts the user to enter
# a series of numbers that selects card to be replaced
# during a drawing phase. The program then prints the new cards.

# Import the random module.
import random


# Create the Deck class.
class Deck():


    def __init__ (self, n_decks=1):

        # Creathe the deck with suits and ranks.
        self.card_list = [num + suit
            for suit in '\u2665\u2666\u2663\u2660'
            for num in 'A23456789TJQK'
            for deck in range(n_decks)]
        
        # Create the empty list of cards dealt.
        self.cards_in_play_list =[]

        # Create the empty list of cards
        # in the discard pile.
        self.discards_list = []
        
        # Shuffle the deck.
        random.shuffle(self.card_list)


    def deal(self):

        # Reshuffle the deck if cards run out.
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        
        # Deal a new card.
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card


    def new_hand(self):

        # Move current cards to discard pile.
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


# Define the play_poker function.
def play_poker_hand(dk):

    # Deal 5 cards into the poker hand.
    hand = [dk.deal() for _ in range(5)]

    # Print the inital hand.
    print("\nInitial Poker Hand:")
    for i, card in enumerate(hand, start = 1):
        print(f"{i}: {card}")
    
    # Ask the user which cards to replace.
    replace_input = input("\nEnter card numbers to replace (ex: 1 3 5), or press Enter to keep all: ")

    # If user selects specific cards, replace them.
    if replace_input.strip() !="":
        indices = list(map(int, replace_input.split()))
        for idx in indices:
            hand[idx - 1] = dk.deal()

    # Print the final hand of cards.
    print("\nFinal Poker Hand:")
    for i, card in enumerate(hand, start = 1):
        print(f"{i}: {card}")


# Define the main function.
def main():

    # Create a single deck.
    dk = Deck(1)

    # Play the hand with the deck.
    play_poker_hand(dk)

# Run the main function
main()