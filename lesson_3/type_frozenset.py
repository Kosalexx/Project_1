my_set_1 = frozenset({1, 2, 3})
my_set_2 = frozenset([1, 4, 19, 20])
my_set_3 = frozenset('asdadsfasdf')
print(my_set_1, my_set_2, my_set_3)
# pамороженные множества являются неизменяемыми
# над ними можно проводить те же операции что и над обычными множествами,
# кроме изменяющих сожержимое
my_set_4 = my_set_1.union(my_set_2)  # объединение заморож. множеств
my_set_5 = my_set_1.difference(my_set_2)  # разность множеств
my_set_6 = my_set_1.symmetric_difference(my_set_2)  # симметрическая разность
my_set_7 = my_set_1.intersection(my_set_2)  # пересечени множеств
print(my_set_4, my_set_5, my_set_6, my_set_7)
set_1 = set('qwerty')
frozenset_1 = frozenset('qwerty')
print(set_1 == frozenset_1)  # сравнение обычного множества и замороженного
# Единственное отличие set от frozenset заключается в том, что set -
# изменяемый тип данных, а frozenset - нет
