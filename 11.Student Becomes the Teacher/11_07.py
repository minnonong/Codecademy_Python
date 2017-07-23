#  11_07 Sending a Letter

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

def average(list_val):
    list_sum = sum(list_val)
    list_len = len(list_val)
    result = list_sum / list_len
    return result

def get_average(dic_val):
    total = 0
    for i in dic_val:
        if(i != "name"):
            list_sum = sum(dic_val[i])
            list_len = len(dic_val[i])
            list_avg = list_sum / list_len
            if (i == "homework"):
                total += list_avg * 0.1
            elif(i == "quizzes"):
                total += list_avg * 0.3
            elif(i == "tests"):
                total += list_avg * 0.6
    return total

def get_letter_grade(score):
    if(score >= 90):
        return "A"
    elif(score >= 80 and score < 90):
        return "B"
    elif(score >= 70 and score < 80):
        return "C"
    elif(score >= 60 and score < 70):
        return "D"
    else:
        return "F"

score = get_average(lloyd)
print get_letter_grade(score)
