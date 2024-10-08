def check_players(num_of_players):
    if num_of_players < 1 or num_of_players > 7:
        print("Error. Not a valid number. Only seven seats open")
        return False
    return True