#  06_10 Ending Up

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = original[0]
    if (first == "a" or first == "e" or first == "i" or first == "o" or first == "u"):
        new_word = word + pyg
    else:
        new_word = original[1:] + original[0] + pyg
    print new_word
else:
    print 'empty'
