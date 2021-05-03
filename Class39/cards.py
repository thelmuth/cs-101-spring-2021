
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
SUITS = ["Spades", "Hearts", "Clubs", "Diamonds"]

def main():
    
#     card = PlayingCard("A", "Spades")
#     print(card)
#     print(card.rank)
#     print(card.suit)
#     print(card.rank_number())

    ### Create a list representing a deck of cards
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            card = PlayingCard(rank, suit)
            deck.append(card)
            
    print(deck)
    
    

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


if __name__ == "__main__":
    main()
    