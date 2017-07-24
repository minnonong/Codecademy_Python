# 12_16 Using strings in lists in functions

n = ["Michael", "Lieberman"]

def join_strings(my_list):
    result = ""
    for i in range(0, len(my_list)):
        result = result + n[i]
    return result

print join_strings(n)
