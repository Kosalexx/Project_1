"""Задание 2. Написать программу для нахождения факториала.
Факториал натурального числа n определяется как произведение всех натуральных чисел от 1 до n включительно.
Реализацию выполнить в виде рекурсивной функции."""

import random  # для проверки работы функции


def factorial_num(n: int) -> int:
    """Вычисляет факториал переданного числа n. """

    if n == 0:
        return 1
    return factorial_num(n - 1) * n  # запускаем рекурсию


num = random.randint(1, 15)  # генерируем случайное число для проверки работы функции
fact_num = factorial_num(num)  # находим факториал нашего числа (вызываем функцию)
print(f'Факториал числа {num} это: {fact_num}')
