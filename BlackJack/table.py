import deck 

class Table():
    def __init__(self):
        self.position = {"Dealer": None,
                         "p_one": None,
                         "P_two": None,
                         "p_three": None,
                         "p_four": None,
                         "p_five": None,
                         "p_six": None,
                         "p_seven": None,}

    #Note: we need to throw exceptions for the case
    #where there is an invalid input for the player
    #this will probably not occus as the sequence will
    #not allow for it but just incase
    def set_card(self, player,card):
        self.position["player"] = card

    def get_card(self, player):
        return self.position["player"]
    
    def test1(self):
        d1 = deck.Deck(list(), list())
        d1.standard_deck()
        self.set_card("p_one", d1.deck[0])
        card = self.get_card("p_one")
        print(card.name, card.color, card.suit, card.value)

T1 = Table()
