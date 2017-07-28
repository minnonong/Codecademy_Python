#  15_10 censor

# 한글 사이트

def censor(text, word):
    list_str = text.split(" ")
    count = 0
    result = ""
    for i in list_str:
        if(i == word and count == 0):
            i = "*" * (len(word))
            count += 1
        result += " " + i
    result = result.strip()
    return result

# 영문 사이트

def censor(text, word):
    text_list = text.split(word)
    result = (len(word) * "*") .join(text_list)
    return result
