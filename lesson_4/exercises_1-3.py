# Задание 1. Создаем три переменные с одинак. данными и одинаковыми идентификаторами (для начала возьмем целые числа)
var_int_1 = 10
var_int_2 = 10
var_int_3 = 10
print(id(var_int_1), id(var_int_2), id(var_int_3), sep='\n', end='\n\n')
# переменные одного НЕИЗМЕНЯЕМОГО типа с одинаковым содержимым (но разным содержанием) будут иметь одинаковый id
# можем проверить тоже и на строковом типе данных
var_str_1, var_str_2, var_str_3 = 'string', 'string', 'string'
print(id(var_str_1), id(var_str_2), id(var_str_3), sep='\n', end='\n\n')
# или на числе с плавающей точкой (тип float)
var_float_1, var_float_2, var_float_3 = 8.31, 8.31, 8.31
print(id(var_float_1), id(var_float_2), id(var_float_3), sep='\n', end='\n\n')
# также это работает на кортежах
var_tuple_1, var_tuple_2, var_tuple_3 = (1, 2, 3, 4, 5), (1, 2, 3, 4, 5), (1, 2, 3, 4, 5)
print(id(var_tuple_1), id(var_tuple_2), id(var_tuple_3), sep='\n', end='\n\n')

# Задание 2. Создаём две переменные с одинаковыми данными и разными id.
# Такая "ситуация" будет с данными ИЗМЕНЯЕМОГО типа. Например списки (тип list):
variable_list_1 = [1, 2, 3, 4, 5]
variable_list_2 = [1, 2, 3, 4, 5]
print(id(variable_list_1), id(variable_list_2), sep='\n', end='\n\n')

# Задание 3. Чтобы переменные из Задания 1 имели разные id (и одинак. содерж.) нужно привести их к ИЗМЕНЯЕМОМУ типу:
var_tuple_1_list = list(var_tuple_1)
var_tuple_2_list = list(var_tuple_2)
var_tuple_3_list = list(var_tuple_3)
print(id(var_tuple_1_list), id(var_tuple_2_list), id(var_tuple_3_list), sep='\n', end='\n\n')
# Переменные из Задания 2 нужно привести к НЕИЗМЕНЯЕМОМУ типу данных
variable_list_1_tuple = tuple([1, 2, 3, 4, 5])
variable_list_2_tuple = tuple([1, 2, 3, 4, 5])
print(variable_list_1_tuple, variable_list_2_tuple)
print(id(variable_list_1_tuple), id(variable_list_2_tuple), sep='\n')  # однако id не стали одинаковыми...
# TODO разобраться, почему id разные
# попробуем тоже действие с set и frozenset
my_set1, my_set2 = {1, 2, 3, 4}, {1, 2, 3, 4}  # создаём 2 множества
froz_my_set1 = frozenset(my_set1)  # изменяем их тип на замороженное множество
froz_my_set2 = frozenset(my_set2)
print(froz_my_set1, froz_my_set2)
print(id(froz_my_set1), id(froz_my_set2))  # ситуация аналогична: переменные имеют разные id
