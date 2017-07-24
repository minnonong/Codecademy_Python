#  12_14 Passing a range into a function

""" range 사용법
          range(a) : 0에서부터 a 이전 까지
          range(a,b) : a에서부터 b 이전 까지
          range(a,b,c): a에서부터 b 이전 까지의 요소를 c 만큼의 간격으로 증가 """

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(0,3))
