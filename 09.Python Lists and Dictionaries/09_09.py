#  09_09 More with 'for'

#  .sort() : 정렬

start_list = [5, 3, 1, 2, 4]
square_list = []

for num in start_list:
    square_list.append(num ** 2)

square_list.sort()

print square_list
