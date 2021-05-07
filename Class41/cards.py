import random

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]

def main():
    
#     card = PlayingCard("A", "Spades")
#     print(card)
#     print(card.rank)
#     print(card.suit)
#     print(card.rank_number())

    ### Create a list representing a deck of cards
#     deck = []
#     for rank in RANKS:
#         for suit in SUITS:
#             card = PlayingCard(rank, suit)
#             deck.append(card)
            
#     deck = Deck()
#     print(deck)
#     print("------------")
#     
#     card = deck.draw_card()
#     print(deck)
#     print(card)
#     
#     print("Cards in the deck:", len(deck))
    
#     steve = Player("Steve")
#     steve.add_card(PlayingCard("Q", "Spades"))
#     steve.add_card(PlayingCard("4", "Diamonds"))
#     
#     print(steve)
#     print(steve.draw_card())
#     print(steve)

    play_war()
    
def play_war():
    """Implements the card game War."""
    
    ### Setup the game
    deck = Deck()
    steve = Player("Steve")
    cheryl = Player("Cheryl")
    
    while len(deck) > 0:
        
        card = deck.draw_card()
        steve.add_card(card)
        
        card = deck.draw_card()
        cheryl.add_card(card)
        
#     print("Deck should now be empty:", deck)
#     print(steve)
#     print(cheryl)

    game_round = 0
    while len(steve) > 0 and len(cheryl) > 0:
        game_round += 1
        
        steve_card = steve.draw_card()
        cheryl_card = cheryl.draw_card()
        
        print()
        print("Round:", game_round)
        print("Steve has", len(steve), "cards and plays", steve_card)
        print("Cheryl has", len(cheryl), "cards and plays", cheryl_card)
        
        if steve_card.rank_number() > cheryl_card.rank_number():
            ## Steve's card was better, he wins this round
            steve.add_card(steve_card)
            steve.add_card(cheryl_card)
            
        elif steve_card.rank_number() < cheryl_card.rank_number():
            ## Cheryl's card was better, he wins this round
            cheryl.add_card(cheryl_card)  
            cheryl.add_card(steve_card)      
    
        else:
            ## This runs if the two cards tie.        
            winner = handle_tie(steve, cheryl)
            winner.add_card(steve_card)
            winner.add_card(cheryl_card)
    
def handle_tie(steve, cheryl):
    """Handles the case where both players tied in this round of War."""
    
    print("Tie! Both players are playing more cards...")
    
    winners_pile = []
    for _ in range(3):
        card_s = steve.draw_card()
        card_c = cheryl.draw_card()
        
        winners_pile.append(card_s)
        winners_pile.append(card_c)
        
    # Draw the card that will try to break the tie
    steve_card = steve.draw_card()
    cheryl_card = cheryl.draw_card()
    
    print("Steve has", len(steve), "cards and plays", steve_card)
    print("Cheryl has", len(cheryl), "cards and plays", cheryl_card)
    
    if steve_card.rank_number() > cheryl_card.rank_number():
        ## Steve's card was better, he wins this round
        winner = steve
        
    elif steve_card.rank_number() < cheryl_card.rank_number():
        ## Cheryl's card was better, he wins this round
        winner = cheryl    

    else:
        ## There's another tie!
        winner = handle_tie(steve, cheryl)
    
    # Add cards to winner's deck
    winner.add_card(steve_card)
    winner.add_card(cheryl_card)
    
    for card in winners_pile:
        winner.add_card(card)
    
    return winner

class PlayingCard:
    """Represents a single playing card from a standard deck."""
    
    def __init__(self, rank, suit):
        """Constructor for the playing card with a given rank and suit."""
        
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        """Returns a string representation of this playing card."""
        return str(self.rank) + " of " + self.suit
    
    def __repr__(self):
        """Returns a string representation of card.
        This is called when printing a list of these things."""
        return str(self.rank) + " of " + self.suit
        
    def rank_number(self):
        """Returns an integer representing the rank of the card.
        Numeric ranks will be themselves.
        J = 11
        Q = 12
        K = 13
        A = 14
        """
        
        if self.rank == "J":
            return 11
        elif self.rank == "Q":
            return 12
        elif self.rank == "K":
            return 13
        elif self.rank == "A":
            return 14
        else:
            return self.rank

class Deck:
    """Represents a deck of cards that can be shuffled and dealt, one card at a time."""
    
    def __init__(self):
        """Initialize a standard 52-card deck and shuffle it."""
        
        self.deck_list = []
        for rank in RANKS:
            for suit in SUITS:
                card = PlayingCard(rank, suit)
                self.deck_list.append(card)
        
        self.shuffle()
        
    def __str__(self):
        return "DECK" + str(self.deck_list)
        
    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.deck_list)

    def draw_card(self):
        """Remove the top card from the deck and return it."""
        return self.deck_list.pop()

    def __len__(self):
        """Returns the number of cards in the deck."""
        return len(self.deck_list)


class Player:
    """Represents a player in the game War, including their pile of cards."""
    
    def __init__(self, name):
        """Player's pile of cards starts empty, and we'll add to it when the game starts."""
        self.name = name
        self.pile = []
        
    def add_card(self, card):
        """Adds a card to this player's pile of cards.
        Adds the card to the bottom of the pile."""
        
        self.pile.insert(0, card)
        
    def draw_card(self):
        """Remove the top card from the pile and return it."""
        return self.pile.pop()

    def __len__(self):
        """Returns the number of cards in the pile."""
        return len(self.pile)
        
    def __str__(self):
        return self.name + str(self.pile)
        
        

if __name__ == "__main__":
    main()
    