# кортежи (тип данных tuple)
empty_tuple = ()  # пустой кортеж
tuple_float = (1.23, 2.34, 5.23)  # кортеж из чисел с плавающей точкой
tuple_names = ('Alexey', 'Nikolai', 'Ales')  # кортеж из строк
info = ('Alexey', 28, 90.5, True)  # кортеж из объектов различных типов
my_tuple = (1,)  # создание кортежа с одним элементом (обязательно ставится запятая)

my_list = [1, 2, 3, 4, 5]
my_tuple_2 = tuple(my_list)  # преобразование списка в кортеж
print(my_tuple_2)

str_text = 'hello world'  # создание кортежа из символов строки
tuple_text = tuple(str_text)
print(tuple_text)

# кортежи поддерживают те же операции что и списки, за исключением изменяющих содержимое
print(info[0], info[2])  # индексация
print(info[:2], info[1:3])  # срезы
print(info.index(28), tuple_text.count('l'))  # методы, такие как count() и index()
print(len(tuple_text), sum(my_tuple_2), max(my_tuple_2), min(my_tuple_2))  # встроенные функции
