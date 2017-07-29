#  17_05

#  리스트 내포(list comprehension): new_list = [x for x in range() if 조건문]

even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print even_squares
