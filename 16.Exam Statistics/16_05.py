#  16_05

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(grades):
    result = 0
    for i in grades:
        result += i

    return result

print grades_sum(grades)

def grades_average(grades):
    sum_result = grades_sum(grades)
    len_list = len(grades)
    result = sum_result / len_list
    return result

print grades_average(grades)
