#  14_15 Counting as you go

#  enumerate(list_name) : 리스트 안의 개별 요소의 색인 제공

choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item
