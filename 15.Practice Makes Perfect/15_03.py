#  15_03 is_int

def is_int(x):
    if(x == 0):
        return True
    elif(x % (x/x) == 0):
        return True
    else:
        return False
        