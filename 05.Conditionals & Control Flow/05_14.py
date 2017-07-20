#  05_14 I Got 99 Problems, But a Switch A...

# 파이썬은 switch문을 사용하지 않고 elif 문만 사용함.

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
