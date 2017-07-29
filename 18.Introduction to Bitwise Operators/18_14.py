#  18_14

def flip_bit(number, n):
    mask = (0b1 << n)
    result = number ^ mask
    return result
