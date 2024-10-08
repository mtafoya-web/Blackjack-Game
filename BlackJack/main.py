import game
import table
import deck 

if __name__ == "__main__":
    #table contains players and dealer
    bj_table = table.Table()

    #Note the two lists are for the deck and discard pile
    std_deck = deck.Deck(list(), list())

    #Total 8 decks
    std_deck.standard_deck()         
    #control variables
    endgame = 0  

    #Start the sequence of the game
    while(endgame < 1):
        game.free_bet(std_deck, bj_table)
