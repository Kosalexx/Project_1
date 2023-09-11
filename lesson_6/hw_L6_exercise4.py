""" Задание 4. Сделать функцию, которая будет вызываться из генератора
списков и по запросу к ней отдавать текущее время с задержкой в 1 сек.
Количество элементов нового списка n запрашивать у пользователя."""
from datetime import datetime
from time import sleep


def datetime_plus_sec() -> str:
    """ Возвращает текущую дату и время в указанном формате,
    после чего "засыпает" на 1 секунду. """
    date_now = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    sleep(1)
    return date_now


def datetime_plus_sec_in_range(n: int) -> list[str]:
    """ Возвращает список из дат и времён с разницей в 1 секунду
    в количестве n элементов."""
    date_list: list[str] = [datetime_plus_sec() for _ in range(n)]
    return date_list


num = int(input())
print(datetime_plus_sec_in_range(num))
