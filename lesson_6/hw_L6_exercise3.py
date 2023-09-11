"""Задание 3. Дан список чисел. Посчитать сколько раз встречается каждое число.
Использовать для подсчёта функцию."""
import random


def count_elements(collection: list | tuple | str)\
        -> dict[str | int | tuple | float, int]:
    """ Принимает в качестве аргумента строку, список или кортеж и возвращает
    словарь, ключами которого являются элементы переданного выражения, а
    значениями - количество вхождений данных элементов.
    ВАЖНО: значениями передаваемых в функцию списка или кортежа должны
    быть объекты неизменяемых типов.
    """
    my_dict: dict[str | int | tuple | float, int] = {}
    for c in collection:
        my_dict[c] = my_dict.setdefault(c, 0) + 1
    return my_dict


rand_list = [random.randint(1, 20) for _ in range(100)]
print(rand_list)
print(count_elements(rand_list), end='\n\n')

my_tuple = (1.23, 2, 3, 5, 10, 32, 1, 20, 10, 32, 5, 5, 5, 10, 1)
print(count_elements(my_tuple), end='\n\n')


my_list_tuple = [(1, 2, 3), (11, 2)]
print(count_elements(my_list_tuple), end='\n\n')
