#  15_08 anti_vowel

def anti_vowel(text):
    result = ""
    for c in text:
        if(c.lower() in "aeiou"):
            c = ""
        else:
            result += c
            
    return result

