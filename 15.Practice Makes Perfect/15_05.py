#  15_05 factorial

def factorial(n):
    result = 1
    if(n >= 2 ):
        while n > 1:
            result *= n
            n -= 1
    else:
        result = n
    return result
