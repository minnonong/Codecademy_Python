#  12_10 Modifying an element of a list in a function

def list_function(my_list):
    my_list[1] = my_list[1] + 3
    return my_list

n = [3, 5, 7]
print list_function(n)
