#  14_08 Your own while / else

from random import randrange

random_number = randrange(1, 10)

count = 0

while count < 3:
    count += 1
    if random_number != guess:
        guess = int(raw_input("Enter a guess:"))
    else:
        print "You Win!"
        break
else:
    print "You lose."
