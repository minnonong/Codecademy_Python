#  15_12 purity

def purify(num_list):
    result = []
    for i in num_list:
        print i
        if(i % 2 == 0):
            result.append(i)
    return result
