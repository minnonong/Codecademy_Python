#  17_12

""" 람다 함수(lambad) : anonymoes function
     lambda x: x % 3 == 0
               ||
     def by_three(x):
          return x % 3 == 0 """

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
