# Создать объект типа bytes можно следующими способами:
# с помощью функции bytes([<Строка>, <Кодировка> [, <Обработка ошибок>]]
text = bytes()  # Если параметры не указаны, то возвращается пустой объект
print(text, type(text))
text_2 = bytes('строка', 'cp1251')  # необходимо передать минимум два первых параметра
print(text_2, type(text))
# Если строка указана только в первом параметре, то возбуждается исключение TypeError.
# В третьем параметре могут быть указаны значения "strict" (при ошибке возбуждается исключение UnicodeEncodeError -
# значение по умолчанию), "replace" (неизвестный символ заменяется символом вопроса)
# или "ignore" (неизвестные символы игнорируются).
print(bytes("string\uFFFD", "cp1251", "replace"))
print(bytes("string\uFFFD", "cp1251", "ignore"))
# c помощью метода строк encode([encoding="utf-8"] [, errors="strict"]) строка преобр. в посл. байтов
# Если кодировка не указана, то строка преобразуется в последовательность байтов в кодировке UTF-8.
bytes_1 = 'строка'.encode()
print(bytes_1, type(bytes))
# указав букву b (регистр не имеет значения) перед строкой в апострофах, кавычках
bytes_2 = b'string'
print(bytes_2, type(bytes_2))
# с помощью функции bytes (<Последовательность>), которая преобразует последовательность целых чисел
# от 0 до 255 в объект типа bytes. Если число не попадает в диапазон, то возбуждается исключение ValueError.
bytes_3 = bytes([225, 226, 224, 174, 170, 160])
print(bytes_3)
print(str(bytes_3, "cp866"))
# с помощью метода bytes.fromhex(<Строка>). Строка в этом случае должна содержать шестнадцатеричные значения символов:
bytes_4 = bytes.fromhex(" e1 e2e0ae aaa0 ")
print(bytes_4)
print(str(bytes_4, "cp866"))
# Объекты типа bytes относятся к последовательностям.
# Каждый элемент такой последовательности может хранить целое число от 0 до 255, которое обозначает код символа.
# Как и все последовательности, объекты поддерживают обращение к элементу по индексу, получение среза, конкатенацию,
# повторение и проверку на вхождение:
bytes_5 = bytes('string', 'cp1251')
print(bytes_5)
print(bytes_5[0])  # обращение по индексу
print(bytes_5[1:5])  # Получение среза
print(bytes_5 + b'123')  # Конкатенация
print(bytes_5*3)  # Повторение
print(115 in bytes_5, b'tr' in bytes_5, b'as' in bytes_5)  # проверка вхождения
# Тип bytes относится к неизменяемым типам. Можно получить значение по индексу, но изменить его нельзя.
# Объекты типа bytes поддерживают большинство строковых методов. Некоторые из этих методов могут некорректно работать
# с русскими буквами - в этих случаях следует использовать тип str, а не тип bytes.
# Не поддерживаются объектами типа bytes строковые методы encode(), isidentifier(), isprintable(), isnumeric(),
# isdecimal(), format_map() и format(), а также операция форматирования.
bytes_6 = bytes("string", "cp1251")
bytes_7 = bytes_6.replace(b'r', b'S')
print(bytes_7)
# Объект типа bytes может содержать как однобайтовые символы, так и многобайтовые.
# При использовании многобайтовых символов некоторые функции могут работать не так, как вы думаете, -
# например, функция len() вернет количество байтов, а не символов:
print(len('строка'))
print(len(bytes('строка', 'cp1251')))
print(len(bytes('строка', 'utf-8')))
#  Преобразовать объект типа bytes в строку позволяет метод decode(). Метод имеет следующий формат:
# decode([encoding="utf-8"][, errors="strict"])
b = (bytes('строка', 'cp1251'))
print(b.decode(encoding='cp1251'), type(b.decode(encoding='cp1251')), b.decode('cp1251'), type(b.decode('cp1251')))