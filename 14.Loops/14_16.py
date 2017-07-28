#  14_16 Multiple lists

#  zip(list1, list2, ...) : 리스트끼리 쌍을 생성하여 더 짧은 쪽의 리스트 끝에서 멈춤.

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if(a >= b):
        print a
    else:
        print b