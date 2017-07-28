#  15_07 reverse

def reverse(text):
    result = ""
    rev_index = len(text) - 1
    for i in range(len(text)):
        result_index = rev_index - i
        result += text[result_index]
    return result
