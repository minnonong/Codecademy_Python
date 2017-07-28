#  15_06 is_prime

def is_prime(x):
    num = x
    count = 0
    if(x > 1):
        while(num > 2):
            num -= 1
            if (x % num == 0):
                count += 1
        if(count == 0):
            return True
        else:
            return False
    else:
        return False
