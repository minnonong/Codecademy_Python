#  15_15 median

def median(user_list):
    sort_list = sorted(user_list)
    len_list = len(user_list)
    div_list = int((len_list) / 2)
    result = sort_list[div_list]

    if (len(user_list) % 2 == 0):
        result += sort_list[div_list - 1]
        result /= 2.0

    return result
