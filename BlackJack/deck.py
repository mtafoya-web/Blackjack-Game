from enum import Enum 
import random 

class Face_cards(Enum):
    ACE = 1
    KING = 10
    QUEEN = 10
    JACK = 10

class Card:
    def __init__(self, color, suit, value):
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
                    self.deck.append(Card(colors[1], i, j))
                else:
                    self.deck.append(Card(colors[0], i, j))
                count += 1

    def print_deck(self):
        count = 0
        for i in self.deck:
            print(i.color, i.suit, i.value)
            count += 1
        print(count)

    def shuffle_deck(self):
        random.shuffle(self.deck)

    #make eight decks
    def standard_deck(self):
        for i in range(8):
            self.set_deck()
    
        

empty_list = []
d1 = Deck(empty_list)
d1.standard_deck()
d1.shuffle_deck()
d1.print_deck()


