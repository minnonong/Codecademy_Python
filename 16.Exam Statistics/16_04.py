#  16_04 

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(grades):
    result = 0
    for i in grades:
        result += i

    return result

print grades_sum(grades)
