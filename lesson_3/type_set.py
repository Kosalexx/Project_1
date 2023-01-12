# множества(тип set)
numbers = {1, 2, 3, 4, 5}
names = {'Alexey', 'Ivan', 'Nikolai'}
info = {'Alexey', 28, 1994, 90.3, (12, 3, 94)}  # элементами множества могут быть только неизменяемые объекты
# множества неупорядочены, поэтому при выводе порядок элементов может отличаться
print(numbers, names, info, sep='\n')
# пустое множество
empty_set = set()
# test = {} - создаст словарь а не множество
myset_1 = set(range(10))
# все элементы множества уникальны, поэтому дубликаты удалятся
myset_2 = set([1, 2, 2, 2, 5, 3, 4, 3, 4, 4, 5, 5])
myset_3 = set('abcdefaaafffdddccc')
myset_4 = set((10, 20, 30, 40, 40, 30))
print(myset_1, myset_2, myset_3, myset_4)
# методы множеств
myset_1.add(12)  # добавление элемента в множество
myset_1.add(13)
myset_1.remove(3)  # удаляет элемент из множества и генерирует ошибку если такого элемента нет
myset_1.discard(4)  # удаляет элемент из множества без генерации ошибки если такого элемента нет
elem = myset_1.pop()  # удаляет и возвращает случайный элемент из множества с генерацией ошибки если множество пустое
print(myset_1)
print(elem)
myset_1.clear()
print(myset_1)  # удаляет все эдементы множества
# операции над множествами
set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {2, 3, 5, 7}
set_3 = {2, 4, 9, 17}
union_set_1 = set_1.union(set_3)  # объединение множеств
union_set_2 = set_1 | set_3  # то же самое что и union
print(union_set_1, union_set_2)
intersect_set_1 = set_1.intersection(set_3)  # пересечение множеств
intersect_set_2 = set_1 & set_3
print(intersect_set_1, intersect_set_2)
diff_set_1 = set_1.difference(set_3)  # разность множеств
diff_set_2 = set_1 - set_3
print(diff_set_1, diff_set_2)
sym_diff_set_1 = set_1.symmetric_difference(set_3)  # симетрическая разность
sym_diff_set_2 = set_1 ^ set_3
print(sym_diff_set_1, sym_diff_set_2)
# предыдущие операции создавали новое множество, ниже будут аналогичные операции, изменяющие исходное множество
set_1.update(set_3)  # объединение множеств (или оператор |=)
print(set_1)
set_1.intersection_update(set_3)  # пересечение множеств (или оператор &=)
print(set_1)
set_1.difference_update(set_2)  # разность (или оператор -=)
print(set_1)
set_1.symmetric_difference_update(set_3)  # симетрич. разность (или оператор ^=)
print(set_1)
set_1.clear()
print(set_1)  # очистить множество
# подмножества и надмножества
set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
set_2 = {2, 3, 5, 7}
print(set_2.issubset(set_1))  # возвращает True если set_2 является подмножеством set_1
print(set_1.issuperset(set_2))  # возвращает True если set_1 является надмножеством set_2
