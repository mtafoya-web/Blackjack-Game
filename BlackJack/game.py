import rules

def free_bet(deck, table):
    num_players = 1
    #Empty the discard pile and shuffle the deck
    deck.discard_to_deck(deck.deck, deck.discard)
    deck.shuffle_deck()

    
    while(rules.check_players(num_players)):
        #Find the num of players
        num_players = int(input("How many players?  "))
    
