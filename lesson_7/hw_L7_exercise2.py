""" Задание 2.
Дан список чисел. Вернуть список, где при помощи функции map()
каждое число переведено в строку. В качестве аргумента функции map()
использовать lambda функцию.
"""
from typing import Union


my_list_num: list[Union[int, float]] = [1, 2, 3, 4, 5, 10, 20, 30, 12.3, 15.7]
my_list_str: list[str] = list(map(lambda x: str(x), my_list_num))
print(my_list_str)
