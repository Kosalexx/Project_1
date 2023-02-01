""" Задание 4.
Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой
строкой которого озаглавив каждый столбец и добавив новый столбец "телефон".
"""

import json
import csv

with open('data_file_ex3.json') as json_file:  # открываем json файл с помощью менеджера контекста
    data = json.load(json_file)  # чтение файла и запись в переменную data

my_dict = data
my_dict_2 = {'111111': '311-11-22', '222043': '222-33-44', '679432': 'None',
             '220004': '12-22-124', '123040': 'None', '633676': '633-67-66'}  # cоздадим словарь с телефонами

with open('data_file_ex4.csv', mode='w', encoding='utf-8') as csv_file:  # создадим и откроем csv файл
    file_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=['id', 'name', 'age', 'phone'])
    file_writer.writeheader()  # печать заголовка
    for key, value in my_dict.items():
        file_writer.writerow({'id': key, 'name': value[0], 'age': value[1], 'phone': my_dict_2[key]})
    # с помощью цикла for "пробегаем" по значениям словаря и записываем их в нужном формате в csv файл
