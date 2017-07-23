#  10_04 Lists + Functions

def fizz_count(x):
    count = 0
    for i in x:
        if(i == "fizz"):
            count += 1
    return count

fizz_count(["fizz", "buzz", "fizz"])
