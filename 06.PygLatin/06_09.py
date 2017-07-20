#  06_09 Move it on Back

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
    word = original.lower()
    first = original[0]
    new_word = word + pyg
    print new_word
else:
    print 'empty'
