#  10_12 Stocking Out

groceries = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def compute_bill(groceries):
    total = 0
    for i in groceries:
        if(stock[i] != 0):
            total += prices[i]
            stock[i] -= 1
    return total

compute_bill(['apple'])
