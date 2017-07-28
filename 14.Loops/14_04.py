#  14_04 Simple errors

choice = raw_input('Enjoying the course? (y/n)')

while choice.lower() != "y" and choice.lower() != "n":
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
