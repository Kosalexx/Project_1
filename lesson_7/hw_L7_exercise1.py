""" Задание 1.
Написать лямбда-функцию определяющую чётное/нечётное. Функция принимает параметр (число)
и если чётное, то выдаёт слово "чётное", если нет - то "нечётное". """

is_even = lambda x: 'чётное' if x % 2 == 0 else 'нечётное'  # лямбда функция.
# принимает число

n = int(input('Введите число целое число: '))  # ввод данных от пользователя

print(is_even(n))  # вывод полученных данных