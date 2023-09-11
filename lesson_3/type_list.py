# создание списка (тип данных list)
numbers = [1, 2, 3, 4, 5]
words = ['hi', 'hello', 'привет']
list_1 = list('list')
print(numbers, words, list_1)
# Пустой список
empty_list_1: list = []
empty_list_2: list = list()
print(empty_list_1, empty_list_2)

numbers_1 = list(range(5))  # генерация списка из чисел от 0 до 4
numbers_2 = list(range(0, 10, 2))  # список чисел от 0 до 10
# (не включительно) с шагом 2
print(numbers_1, numbers_2)

# генерация списка четных числе от 2 до 50
list_2 = [i for i in range(1, 51) if i % 2 == 0]
print(list_2)
print(len(list_2))  # печать длины списка

# индексация
print(list_2[0], list_2[5], list_2[10], list_2[18])
# срезы
print(list_2[2:19])
print(list_2[10:])
print(list_2[:6])
# функции и методы списков
list_3 = list()
list_3.append(2)  # добавление элемента в конец списка
list_3.append(4)
list_3.append(6)
print(list_3)
list_3[0] = 999  # списки - изменяемы. Изменяем элемент по его индексу
print(list_3)
list_4 = [10, 1923, 123, 125, 1233]
list_3.extend(list_4)  # добавление списка list_4 в конец списка list_3
print(list_3)
# разница между append() и extend()
words_1 = ['qwe', 'asd', 'zxc']
words_2 = ['abc', 'def', 'qdx']
words_1.append('Python')  # 'Python' добавится как отдельный элемент списка
words_2.extend('Python')  # в список добавятся 'P', 'y', 't', 'h', 'o', 'n'
print(words_1, words_2, sep='\n')
# вывод списка (без квадратных скобок)
print(*words_1)  # распаковка
for i in range(len(words_1)):  # вывод с помощью цикла
    print(words_1[i], end=' ')
print()

for word in words_1:  # вывод с помощью цикла
    print(word, end=' ')
print()
# методы списков
words_1.insert(0, 'asdqq')  # вставляем значение по индексу
print(words_1)
print(words_1.pop(1))  # удаляет элемент из списка по указанному индексу
# и возвращает его значение
words_1.remove('Python')  # удаляет первый лемент в списке,
# имеющий переданный в метод значение
print(words_1)
words_1.clear()  # очищает список
print(words_1)
