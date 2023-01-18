import timeit

# для измерения среднего времени выполнения куска кода предназначена функция timeit.timeit()
""" Cинтаксис функции timeit() модуля timeit

timeit.timeit(stmt='pass', setup='pass', 
              timer=<default timer>, 
              number= 1000000, globals=None))
               
ПАРАМЕТРЫ:
stmt='pass' - проверяемый код
setup='pass' - настройка кода,
timer=<default timer> - используемый таймер,
number=1000000 - число циклов измерений,
globals=None - область видимости.
ВОЗВРАЩАЕМОЕ ЗНАЧЕНИЕ:
float время выполнения кода в цикле number раз."""

# с помощью этого метода мы можем замерять время выполнения различных вариантов исполнения одной и той же задачи
# например вывода слов из задания 1
word_1 = 'hello'
word_2 = 'world'
text_kon = '!' + word_2 + ' ! ' + word_1 + '!'
text_format = '!{} ! {}!'.format(word_2, word_1)
text_f = f'!{word_2} ! {word_1}!'
print(timeit.timeit(stmt="'!' + word_2 + ' ! ' + word_1 + '!'", setup='word_2 = "world"; word_1 = "hello"'))
print(timeit.timeit(stmt="'!{} ! {}!'.format(word_2, word_1)", setup='word_2 = "world"; word_1 = "hello"'))
# мы также можем задать переменные через globals если они были объявлены ранее вне timeit()
print(timeit.timeit(stmt="f'!{word_2} ! {word_1}!'", globals=globals()))  # или можно задать переменные через setup


# как видим f-строки работают практически в 2 раза быстрее ;)

# попробуем измерять скорость выполнения объявленных функций
def my_function_1():  # функция, считающая сумму всех чисел от 0 до 100 с использованием цикла for
    total = 0
    for i in range(100 + 1):
        total += i
    return total


def my_function_2():  # функция, считающая сумму всех чисел от 0 до 100 с использованием цикла while
    total = 0
    counter = 0
    while counter < 100:
        counter += 1
        total += counter
    return total


print(my_function_1(), my_function_2())  # как видим, обе функции делают то же самое
# измеряем время выполнения каждой функции, узнаем какой цикл будет работать быстрее
print('Цикл for: ', timeit.timeit(stmt='my_function_1()', number=10000, globals=globals()))
print('Цикл while: ', timeit.timeit(stmt='my_function_2()', number=10000, globals=globals()))
# можем сделать вывод, что цикл for работает быстрее


# создадим функцию, выдающую n-ый элемент последовательности Фибоначчи:
def fibonacci_number(n):  # функция принимает значение n и возвращает n-ый элемент последовательности
    n = n - 2
    fib1 = fib2 = 1
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


def fibonacci_number_rec(n):  # функция выводит n-ый элемент последовательности Фибоначчи при помощи
    if n in (1, 2):
        return 1
    return fibonacci_number_rec(n - 1) + fibonacci_number_rec(n - 2)
# Данный метод должен работать медленнее из-за самой природы рекурсии. Давайте это проверим.


print(fibonacci_number(15), fibonacci_number_rec(15))  # как видно, обе функции приводят к одинаковому результату
# проверим скорость их работы
print('Функция с циклом: ', timeit.timeit(stmt='fibonacci_number(n)', setup='n = 15', number=1000, globals=globals()))
print('Рекурс. ф-ция: ', timeit.timeit(stmt='fibonacci_number_rec(n)', setup='n = 15', number=1000, globals=globals()))
# Мы можем сделать вывод, что рекурсивная функция будет выполняться дольше
