#  14_12 For your A

#  print "문자열", : 개행 없이 한 줄에 입력.

s = "A bird in the hand..."

s = s.replace(" ", "")

for i in s:
    if(i.lower() == "a"):
        print 'X',
    elif(i == " "):
        print "",
    else:
        print i,

print ""
