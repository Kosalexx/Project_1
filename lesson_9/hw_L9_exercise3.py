"""ЗАДАНИЕ 3
Программа на вход должна принимать файл с каким-то текстом. Пользователь
вводит любую английскую букву. Программа должна считать сколько раз эта
буква встречается в тексте (без учёта регистра). То есть буквы n и N
считать одинаковыми.

Пример работы:
Введите букву: n
Результат: буква встречается 124 раза в тексте.
"""


def count_letter(text: str) -> int:
    """Counts how many times a letter appears in a text."""
    letter = input('Input a letter: ')
    # version 1: первый пришедший в голову вариант
    # counter = 0
    # for symbols in text:
    #     if symbols.lower() == letter.lower():
    #         counter += 1
    # version 2: вспомнил про метод count()
    counter = text.count(letter.lower()) + text.count(letter.upper())
    result = f'The letter appears {counter} times in the text.'
    return result


text_file = open('text_file(ex3).txt', 'r')
some_text = text_file.read()
print(count_letter(some_text))
