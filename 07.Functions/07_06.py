#  07_06 Practice Makes Perfect

def cube(n):
    result = n ** 3
    return result

def by_three(n):
    if (n % 3 == 0):
        return cube(n)
    else:
        return "False"
