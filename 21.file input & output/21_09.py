#  21_09

with open("text.txt", "w") as my_file:
    my_file.write("Hello!")

print my_file.closed

if(my_file.closed == False):
    my_file.close()
