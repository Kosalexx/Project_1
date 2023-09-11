# Задание 1. Создаем три переменные с одинак. данными и одинаковыми
# идентификаторами (для начала возьмем целые числа)
var_int_1 = 10
var_int_2 = 10
var_int_3 = 10
print(id(var_int_1), id(var_int_2), id(var_int_3), sep='\n', end='\n\n')

var_str_1, var_str_2, var_str_3 = 'string', 'string', 'string'
print(id(var_str_1), id(var_str_2), id(var_str_3), sep='\n', end='\n\n')

var_float_1, var_float_2, var_float_3 = 8.31, 8.31, 8.31
print(id(var_float_1), id(var_float_2), id(var_float_3), sep='\n', end='\n\n')

var_tuple_1, var_tuple_2 = (1, 2, 3, 4, 5), (1, 2, 3, 4, 5)
var_tuple_3 = (1, 2, 3, 4, 5)
print(id(var_tuple_1), id(var_tuple_2), id(var_tuple_3), sep='\n', end='\n\n')

# Задание 2. Создаём две переменные с одинаковыми данными и разными id.
variable_list_1 = [1, 2, 3, 4, 5]
variable_list_2 = [1, 2, 3, 4, 5]
print(id(variable_list_1), id(variable_list_2), sep='\n', end='\n\n')

# Задание 3. Чтобы переменные из Задания 1 имели разные id (и одинак. содерж.)
var_tuple_1_list = list(var_tuple_1)
var_tuple_2_list = list(var_tuple_2)
var_tuple_3_list = list(var_tuple_3)
print(id(var_tuple_1_list), id(var_tuple_2_list), id(var_tuple_3_list),
      sep='\n', end='\n\n')

variable_list_1_tuple = tuple([1, 2, 3, 4, 5])
variable_list_2_tuple = tuple([1, 2, 3, 4, 5])
print(variable_list_1_tuple, variable_list_2_tuple)
print(id(variable_list_1_tuple), id(variable_list_2_tuple), sep='\n')
my_set1, my_set2 = {1, 2, 3, 4}, {1, 2, 3, 4}
froz_my_set1 = frozenset(my_set1)
froz_my_set2 = frozenset(my_set2)
print(froz_my_set1, froz_my_set2)
print(id(froz_my_set1), id(froz_my_set2), end='\n\n')

my_list_1 = ['1']
my_list_2 = ['1']
print(type(my_list_1), id(my_list_1))
print(type(my_list_2), id(my_list_2))
my_str_1 = str(my_list_1)
my_str_2 = str(my_list_1)
print(my_str_1, type(my_str_1), id(my_str_1), sep='--')
print(my_str_2, type(my_str_2), id(my_str_2), sep='--')

my_bool_1 = bool(my_list_1)
my_bool_2 = bool(my_list_2)
print(my_bool_1, type(my_bool_1), id(my_bool_1), sep='--')
print(my_bool_2, type(my_bool_2), id(my_bool_2), sep='--')
