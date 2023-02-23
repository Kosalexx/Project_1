"""ЗАДАНИЕ 3
Программа на вход должна принимать файл с каким-то текстом. Пользователь
вводит любую английскую букву. Программа должна считать сколько раз эта
буква встречается в тексте (без учёта регистра). То есть буквы n и N
считать одинаковыми.

Пример работы:
Введите букву: n
Результат: буква встречается 124 раза в тексте.
"""


def count_letter(text: str, sym: str) -> int:
    """Counts how many times a letter appears in a text."""

    counter = text.count(sym.lower()) + text.count(sym.upper())
    return counter


result = 0
with open('text_file(ex3).txt') as file:
    letter = input('Input a letter: ')
    for line in file:
        result += count_letter(line, letter)
print(f'Entered letter "{letter}" appears {result} times in text.')
