string_1 = input('Введите первую строку: ')
string_2 = input('Введите вторую строку: ')
string_3 = input('Введите третью строку: ')
string_4 = input('Введите четвертую строку: ')

file_1 = open('text_file.txt', 'w')  # создаст и откроет для записи файл
file_1.write(string_1 + '\n')  # запись 1-й строки
file_1.write(string_2 + '\n')  # запись 2-й строки
file_1.close()  # закрытие файла

with open('text_file.txt', 'a') as file_1:   # 'a'  - открытие на дозапись
    file_1.write(string_3 + '\n')  # запись 3-й строки
    file_1.write(string_4 + '\n')  # запись 4-й строки

with open('text_file.txt', 'r') as f:
    print(f.readlines())
