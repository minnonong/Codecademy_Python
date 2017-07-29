#   16_08

import math

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

def grades_variance(grades, average):
    variance = 0
    for i in grades:
        variance += ((average - i) ** 2)
        variance = variance / len(grades)
    return variance

print grades_variance(grades,  grades_average(grades))

def grades_std_deviation(variance):
    result = math.sqrt(variance)
    return result

print grades_std_deviation(grades_variance(grades,  grades_average(grades)))
