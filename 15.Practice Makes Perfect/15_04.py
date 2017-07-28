#  15_04 digit_sum

def digit_sum(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    print sum
    return sum

# floor divide 이용 
#
# def digit_sum(n):
#     count = len(str(n)) - 1
#     num = n
#     result = 0
#     for i in range(len(str(n))):
#         div_num = num // 10 ** count
#         result += div_num
#         mod_num = n % 10 ** count
#         num = mod_num
#         count -= 1
#     print result
#     return result
