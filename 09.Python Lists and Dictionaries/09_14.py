#  09_14 Remove a Few Things

#  del() : 키 값을 기준으로 삭제
#  remove() : 값을 기준으로 삭제

inventory = {'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'],
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

inventory['pouch'].sort()

inventory['pocket'] = ['seashell', 'strangeberry', 'lint']

inventory['backpack'].sort()

inventory['backpack'].remove('dagger')

inventory['gold'] + 50
