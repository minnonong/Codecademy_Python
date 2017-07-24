#  12_11 List manipulation in functions

n = [3, 5, 7]

def list_extender(my_list):
    my_list.append(9)
    return my_list

print list_extender(n)
