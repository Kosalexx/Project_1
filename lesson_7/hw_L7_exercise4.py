""" Задание 4.
Написать декоратор к двум любым функциям, который бы считал и выводил время их выполнения.
"""

from time import time
from random import randint


def decorator_time(func):
    """ Выводит время, затраченное на выполнение переданной функции."""

    def wrapper(*args, **kwargs):
        """ Обёртка. """

        print(f'Выполняем функцию {func.__name__}.')
        start = time()
        result_func = func(*args, **kwargs)
        end = time()
        print(f'Время выполнения функции {func.__name__}: {end - start} секунд.', end='\n\n')
        return result_func

    return wrapper


""" Для проверки работы нашего декоратора используем функции, написанные в предыдущих уроках."""


@decorator_time
def factorial_num(n: int) -> int:
    """Вычисляет факториал переданного числа n. """

    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


@decorator_time
def fibonacci_number(n: int) -> int:
    """ Вычисляет n-ый элемент последовательности Фибоначчи. """

    n = n - 2
    fib1 = fib2 = 1
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


num = randint(1, 50)  # генерируем случайное число
fact_num = factorial_num(num)
fib_num = fibonacci_number(num)

print('Результаты выполнения функций:')
print(f'Факториал числа {num} это: {fact_num}')
print(f'{num}-й элемент последовательности Фибоначчи: {fib_num}')
