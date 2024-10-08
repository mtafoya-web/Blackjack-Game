import rules

def first_two_cards(deck, table, num_players):
    #Keeps track the dealer recives only two cards
    dealer_count = 0

    #we double the amount of the loop to give two cards
    #to every player
    for i in range(num_players*2):
        #variable will keep track who get the card
        j = i 
        #check if we are passed the amount of players
        #offsets the amount to give card to the correct player
        if i >= num_players:
            j = i - num_players
        #players start from value 1 so gives card to the player    
        table.position[j+1].append(deck.get_card())
        #checking the dealer only gets two cards
        if dealer_count < 2:
            table.position["Dealer"].append(deck.get_card())
            dealer_count += 1

        

def free_bet(deck, table):
    num_players = None
    #Empty the discard pile and shuffle the deck
    deck.discard_to_deck(deck.deck, deck.discard)
    deck.shuffle_deck()

    
    while(rules.check_players(num_players) == False):
        #Find the num of players
        try:
            num_players = int(input("How many players?  "))
        except:
            print("Please Enter An number 1 - 7")
    
    #Give the first two cards
    first_two_cards(deck, table, num_players)

    #Print first two cards
    table.print_all_player_cards()


    #check for natural blackjack
    for i in range(num_players):     
        curr = table.position[i+1]
        sum  = rules.BlackJackRules.get_sum(curr[0].value, curr[1].value)
        rules.BlackJackRules.check_natural_bj(sum, i+1, curr)
        table.position["Count"].append(sum)

    
    print(table.position["Dealer"],"\n ", table.position[1], "\n ", table.position[2], "\n ", table.position[3], "\n ", table.position[4], "\n ", table.position[5] ,"\n ", table.position[6], "\n ", table.position[7], "\n ", table.position["Count"])
    

    
