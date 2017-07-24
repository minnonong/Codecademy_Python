#  12_13 Modifying each element in a list in a function

n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(n)):
        n[i] = n[i] * 2
    return x

print double_list(n)
