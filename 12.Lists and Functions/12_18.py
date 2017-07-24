# 12_18 Using a list of lists in a function

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(my_list):
    result = []
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list[i])):
            result.append(my_list[i][j])
    return result

print flatten(n)
