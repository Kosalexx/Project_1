import timeit

word_1 = 'hello'
word_2 = 'world'
text_kon = '!' + word_2 + ' ! ' + word_1 + '!'
text_format = '!{} ! {}!'.format(word_2, word_1)
text_f = f'!{word_2} ! {word_1}!'
print(timeit.timeit(stmt="'!' + word_2 + ' ! ' + word_1 + '!'",
                    setup='word_2 = "world"; word_1 = "hello"'))
print(timeit.timeit(stmt="'!{} ! {}!'.format(word_2, word_1)",
                    setup='word_2 = "world"; word_1 = "hello"'))

print(timeit.timeit(stmt="f'!{word_2} ! {word_1}!'",
                    globals=globals()))
# как видим f-строки работают практически в 2 раза быстрее
# попробуем измерять скорость выполнения объявленных функций


def my_function_1() -> int:
    total: int = 0
    for i in range(100 + 1):
        total += i
    return total


def my_function_2() -> int:
    total: int = 0
    counter: int = 0
    while counter < 100:
        counter += 1
        total += counter
    return total


print(my_function_1(), my_function_2())
print('Цикл for: ', timeit.timeit(stmt='my_function_1()',
                                  number=10000, globals=globals()))
print('Цикл while: ', timeit.timeit(stmt='my_function_2()',
                                    number=10000, globals=globals()))
# можем сделать вывод, что цикл for работает быстрее


# создадим функцию, выдающую n-ый элемент последовательности Фибоначчи:
def fibonacci_number(n: int) -> int:
    n = n - 2
    fib1: int = 1
    fib2: int = 1
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


def fibonacci_number_rec(n: int) -> int:
    if n in (1, 2):
        return 1
    return fibonacci_number_rec(n - 1) + fibonacci_number_rec(n - 2)
# Данный метод должен работать медленнее из-за самой природы рекурсии.


print(fibonacci_number(15), fibonacci_number_rec(15))
# проверим скорость их работы
print('Функция с циклом: ', timeit.timeit(stmt='fibonacci_number(n)',
                                          setup='n = 15',
                                          number=1000,
                                          globals=globals()))
print('Рекурс. ф-ция: ', timeit.timeit(stmt='fibonacci_number_rec(n)',
                                       setup='n = 15',
                                       number=1000,
                                       globals=globals()))
