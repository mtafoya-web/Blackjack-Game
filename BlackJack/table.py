import deck 
from enum import Enum 

class Players(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7


class Table():
    def __init__(self):
        #Key will be a list of cards
        self.position = {"Dealer": list(),
                         Players.ONE.name: list(),
                         Players.TWO.name: list(),
                         Players.THREE.name: list(),
                         Players.FOUR.name: list(),
                         Players.FIVE.name: list(),
                         Players.SIX.name: list(),
                         Players.SEVEN.name: list()}

    #Note: we need to throw exceptions for the case
    #where there is an invalid input for the player
    #this will probably not occur as the sequence will
    #not allow for it but just incase
    def set_card(self, player, card):
        self.position[player].append(card)
        

    def get_cards(self, player):
        return self.position[player]
    
    def test1(self):
        d1 = deck.Deck(list(), list())
        d1.standard_deck()
        self.set_card('ONE', d1.deck[0])
        self.set_card('ONE', d1.deck[2])
        cards = self.get_cards('ONE')
        #show the objects in our dictionary and the derefrenced objects.
        print(self.position['ONE'])
        for card in cards:
            print(card.name, card.color, card.suit, card.value)
        
        

#T1 = Table()
#T1.test1()
