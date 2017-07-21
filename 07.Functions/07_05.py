#  07_05 Functions Calling Functions

def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2
