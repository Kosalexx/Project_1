""" Изучение и написание простого декоратора.
Декоратор — это функция, которая позволяет обернуть другую функцию для
расширения её функциональности без непосредственного изменения её кода.

 Для проверки работы декоратора используем функцию по нахождению
 факториала из задания 2 ДЗ."""

import random


def robot_decorator(func):
    """ Сам декоратор """
    def wrapper(*args, **kwargs):
        """ Обёртка.
        "Декорируемая" функция, принимающая аргументы для своей работы
         не будет работать без (*args, **kwargs) в "скобках" wrapper"""
        from time import sleep

        print('Начинаю калибровку!')
        sleep(1)
        print('Готов к работе.')
        sleep(0.3)
        print(f'Выполняю функцию: {func} ...')
        sleep(1)
        result = func(*args, **kwargs)  # указывается *args, **kwargs
        print('Готово! Функция выполнена.')
        sleep(0.3)
        print('Работа завершена')
        return result

    return wrapper


@robot_decorator
def factorial_num(n: int) -> int:
    """Вычисляет факториал переданного числа n. """
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


@robot_decorator
def empty_function() -> None:
    """ Написал эту функцию-пустышку для проверки работы декоратора в котором в функции-обёртке
    в wrapper(*args, **kwargs) ожидаются аргументы *args и **kwargs."""
    print('Функция без аргументов вызвана. ')


num = random.randint(1, 15)  # генерируем случайное число
fact_num = factorial_num(num)
empty_function()

print(f'Факториал числа {num} это: {fact_num}')
