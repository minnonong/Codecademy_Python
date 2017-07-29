#  18_11

def check_bit4(user_int):
    mask = 0b1000
    result = user_int & mask
    result = result >> 3
    if(result == 1):
        return "on"
    else:
        return "off"

print check_bit4(0b1)
