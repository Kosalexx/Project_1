"""
Задание 5:
Реализуем ввод от пользователя 2х целых чисел.
Условие первое: Осуществляем проверку чисел на равенства (текст вывода = Числа равны)
Условие второе: Осуществляем проверку что первое число больше второго (текст вывода = Первое число больше второго)
Условие третье: Осуществляем проверку для остальных вариантов (текст вывода = Отработала секция else)
"""

num_1 = int(input())
num_2 = int(input())

if num_1 == num_2:
    print('Числа равны')
elif num_1 > num_2:
    print('Первое число больше второго')
else:
    print('Отработала секция else (Второе число больше первого)')
# TODO переписать программу в виде функции (def number_comprassion(x, y))
