#  12_17 Using two lists as two arguments in a function

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
    for i in range(0, len(y)):
        x.append(y[i])
    return x
print join_lists(m, n)
