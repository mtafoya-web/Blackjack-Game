from enum import Enum 
import random 

class Face_cards(Enum):
    ACE = 1
    KING = 10
    QUEEN = 10
    JACK = 10

class Card:
    def __init__(self, name, color, suit, value):
        self.name = name 
        self.color = color
        self.value = value
        self.suit = suit
    
    def set_color(self, color):
        self.color = color
    def set_value(self, value):
        self.value = value 
    def set_suit(self, suit):
        self.suit = suit

class Deck:
    def __init__(self, deck):
        self.deck = [] #EMPTY LIST

    def set_deck(self):
        count = 0
        colors = ["Red", "Black"]
        suits = ["Clubs", "Dimonds", "Hearts", "Spades"]

        for i in suits:
            #Iterate through the numerical value of the cards
            for j in range(1, 14):
                #Color the card 
                if i == "Clubs" or i == "Spades":
                    self.deck.append(Card(j, colors[1], i, j))
                else:
                    self.deck.append(Card(j, colors[0], i, j))
                
                count += 1
            
        for k in self.deck:
            if k.value == 1:
                k.name = Face_cards.ACE.name
            elif k.value == 11:
                k.name = Face_cards.JACK.name
                k.value = 10
            elif k.value == 12:
                k.name = Face_cards.QUEEN.name
                k.value = 10
            elif k.value == 13:
                k.name = Face_cards.KING.name
                k.value = 10
  
    def print_deck(self):
        count = 0
        for i in self.deck:
            print(i.name, i.color, i.suit, i.value)
            count += 1
        print("Total number of Cards: ", count)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    #make eight decks
    def standard_deck(self):
        for i in range(8):
            self.set_deck()

    def test_fiftytwo(self):
        print("***52 CARD DECK***")
        self.set_deck()
        self.print_deck()
        print("Now shuffled deck...")
        self.shuffle_deck()
        self.print_deck()

d1 = Deck(list())
d1.test_fiftytwo()

