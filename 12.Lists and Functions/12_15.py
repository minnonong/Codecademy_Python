#  12_15 Iterating over a list in a function

n = [3, 5, 7]

def total(n):
    result = 0
    for i in range(0, len(n)):
        result += n[i]
    return result

print total(n)
