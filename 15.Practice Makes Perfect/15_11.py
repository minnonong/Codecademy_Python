#  15_11 count

def count(sequence, item):
    found = 0
    for i in sequence:
        if(i == item):
            found += 1
            
    return found
