""" Изучение и написание простого декоратора.
Декоратор — это функция, которая позволяет обернуть другую функцию для
расширения её функциональности без непосредственного изменения её кода.

Для проверки работы декоратора используем функцию по нахождению
факториала из задания 2 ДЗ."""
import random
from time import sleep
from typing import Callable, TypeVar, ParamSpec


P = ParamSpec('P')
RT = TypeVar('RT')


def robot_decorator(func: Callable[P, RT]) -> Callable[P, RT]:
    """ Сам декоратор """
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> RT:
        """ Обёртка."""

        print('Начинаю калибровку!')
        sleep(1)
        print('Готов к работе.')
        sleep(0.3)
        print(f'Выполняю функцию: {func} ...')
        sleep(1)
        result = func(*args, **kwargs)
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


num = random.randint(1, 15)
fact_num = factorial_num(num)

print(f'Факториал числа {num} это: {fact_num}')
