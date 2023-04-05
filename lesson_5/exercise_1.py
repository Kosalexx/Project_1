"""Задание 1.
Ввести предложение состоящее из двух слов. Поменять местами слова,
добавить восклицательный знак в начало и конец,
слова разделить тремя символами (пробел, восклицательный знак и ещё пробел),
вывести итоговое предложение на экран.
Задание необходимо выполнить тремя разными способами форматирования.
"""

text = input('Введите предложение из двух слов: ')
word_1, word_2 = [c for c in text.split()]
# Cпособ 1: вывод при помощи конкатенации строк
print('!' + word_2 + ' ! ' + word_1 + '!')
# Способ 2: использование форматирования .format()
print('!{} ! {}!'.format(word_2, word_1))
# Способ 3: использование f-строк
print(f'!{word_2} ! {word_1}!')
