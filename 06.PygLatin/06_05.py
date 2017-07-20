#  06_05 Check Yourself... Some More

#  .isalpha() : 값이 알파벳 문자로만 구성되어있는지 확인하는 메소드

original = raw_input("Input: ")

if len(original) > 0 and original.isalpha():
    print original
else:
    print "empty"
