#  15_14 remove_duplicates

def remove_duplicates(user_list):
    result_list = []
    for i in user_list:
        if(i not in result_list):
            result_list.append(i)

    return result_list
