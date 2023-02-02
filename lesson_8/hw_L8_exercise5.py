""" Задание 5.
Прочитать сохранённый csv-файл и сохранить данные в excel-файл, кроме возраста - столбец с этими данными
не нужен.
"""

import csv
import openpyxl
import string

wb = openpyxl.Workbook()  # Делаем активной рабочую книгу
wb.create_sheet('Page1', 0)  # Создаем страницу с заданным названием, и помещаем ее на первое место
wb.save('data_file_ex5.xlsx')  # Сохраняем файл
wb = openpyxl.load_workbook('data_file_ex5.xlsx')  # Открываем файл
wb.create_sheet('Page1')  # Создаем таблицу
worksheet = wb['Page1']  # Делаем таблицу активной

""" Считывание данных из csv файла и запись во вложенный список."""
with open('data_file_ex4.csv', encoding='utf-8') as csv_file:
    file_reader = csv.reader(csv_file)
    my_data = []
    for row in file_reader:
        # worksheet.append(row) - мы могли здесь и закончить, если бы нужно было записать в excel весь csv файл
        # в котором первый список занял бы первый ряд (А1-D1) (по условию наоборот), поэтому пойдём другим путём
        my_data.append(row)

""" Запись полученного списка в Excel файл.  """
letters = string.ascii_uppercase
for i in range(len(my_data)):
    for c in range(len(my_data[i])):
        if c < 2:  # пропускаем строку с возрастом (по условию задачи)
            worksheet[f'{letters[i]}{c + 2}'] = my_data[i][c]
        elif c > 2:
            worksheet[f'{letters[i]}{c + 1}'] = my_data[i][c]

wb.save('data_file_ex5.xlsx')  # cохраняем изменения в excel файле
