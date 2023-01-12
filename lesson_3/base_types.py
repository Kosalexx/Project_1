# int, float, bool, str
int_1 = 5
float_1 = 3.14
print(type(int_1))
print(type(float_1))

int_2 = int(float_1)  # преобразование числа в целочисленный тип данных, число округляется в меньшую сторону
print(int_2)

float_2 = float(int_1)  # преобразование числа в число с плавающей точкой (тип float)
print(float_2)

float_3 = 10 / 5  # в результате деления одного целого числа на другое получается число с плавающей точкой
print(float_3)
print(type(float_3))

# арифметические операции с int и float
num_1 = 5 ** 2  # возведение в степень
num_2 = 4 + 7  # сложение
num_3 = 31 - 2  # вычетание
num_4 = 12 * 4  # умножение
num_5 = 12 / 3  # деление (результат - число с плавающей точной (тип float))
num_6 = 12 % 5  # деление по модулю (возвращает остаток от деления)
num_7 = 25 // 7  # целочисленное деление
print(num_1, num_2, num_3, num_4, num_5, num_6, num_7)

# тип bool: имеет 2 значения (True / False)
bool_1 = True
bool_2 = False
print(type(bool_1), type(bool_2))
print(bool(1), bool(0), bool(5), bool('asd'))  # возвращает False если в bool() передается 0 и True в остальных случаях
# также булевый тип данных возвращается при сравнении элементов
bool_3 = num_2 > num_1
bool_4 = num_3 > num_2
print(bool_3, type(bool_3), bool_4)

# str
text = 'hello world'
print(type(text))
print(text[0] + text[3] + text[6] + text[6])  # str объекты индексируются, можно собрать другое "слово" зная индексы
print(len(text))  # длина объекта
text_2 = str(num_4)  # преобразование числа(класс int) в строку(класс str)
print(text_2, type(text_2))
# некоторые функции и методы строк
text_3 = 'hello world'.upper()  # переводит строку в верхний регистр
text_4 = text_3.lower()  # переводит строку в нижний регистр
text_5 = text_4.replace('h', 'g')  # заменяет один символ строки другим
bool_5 = text_5.isdigit()  # возвращает True если строка состоит из чисел
bool_6 = 'world'.isalpha()  # возвращает True если строка состоит из букв
bool_7 = text_5.isalpha()  # в строке есть пробел, поэтому вернет False
print(text_3, text_4, text_5, bool_5, bool_6, bool_7)
# удаление лишних символо в конце и начале строки (по умолчанию - пробел, иное - передается в кач-ве аргумента метода
text_6 = '     Какой-то текст и много пробелов в конце и начале         '.strip()
print(text_6)

text_7 = 'Здесь просто должен быть какой-то текст'
list_1 = text_7.split()  # разбивает строку на слова по аргументу передаваемому в метон(по умолч. - пробел)
print(list_1)
text_8 = ' '.join(list_1)  # обратный методу split()
print(text_8, type(text_8))
