import table 

def check_players(num_of_players):
    try:
        if num_of_players < 1 or num_of_players > 7:
            print("Error. Not a valid number. Only seven seats open")
            return False
        return True
    #The user typed in a letter or character
    except TypeError:
        return False

#A utility class only has methods are static to be called
# without creating an object   
class BlackJackRules():
    """A utility class with basic black-jack rules"""
    
    #choose the value of ACE 1 or 11
    @staticmethod
    def ace_value(card):
        new_value = 0
        while(new_value != 1 or new_value != 11):
            try:
                new_value = int(input("Choose the value of your Ace 1 or 11"))
            except:
                print("Enter a valid number")
        return new_value       

    #Function is going to sum n number of argumets using *args
    @staticmethod
    def get_sum(*args):
        sum = 0
        for num in args:
            sum += num
        return sum

    @staticmethod
    def check_natural_bj(sum, player_num, player):                
        if (sum == 11 or sum == 21) and (player[0] == 1 or player[1] == 1):
            print("Congrats", player_num, " you got Natural BlackJack")

        
