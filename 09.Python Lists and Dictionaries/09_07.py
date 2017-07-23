#  09_07 Maintaining Order

#  list_name.index(찾는 요소) : 리스트 내에 찾는 요소 검색
#  list_name.insert(index, 추가 할 요소) : 해당 index에 추가 요소를 넣고
#                                         기존에 해당 index에 있던 요소는 한 칸 뒤로 밀기

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]

duck_index = animals.index("duck")# Use index() to find "duck"

animals.insert(duck_index,"cobra")
print animals
