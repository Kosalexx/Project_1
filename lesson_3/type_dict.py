# словари(тип данных dict)
empty_dict: dict = {}  # создание пустого словаря
empty_dict_2: dict = dict()
print(type(empty_dict))
# создание словаря
dict_1 = {'dict': 1, 'dictionary': 2}
dict_2 = {}
dict_2['dict'] = 1
dict_2['dictionary'] = 2
print(dict_1, dict_2)
info = dict(name='Alexey', age=28)
info_2 = dict([('name', 'Alexey'), ('age', 28)])
print(info, info_2)
my_dict = {a: a ** 2 for a in range(7)}
my_dict_2 = dict.fromkeys(['name', 'age', 'job'], None)
print(my_dict, my_dict_2)
# доступ к объектам происходит по ключу
print(f'I am {info["name"]}. I am {info["age"]} years old.')
print(len(my_dict))  # длина словаря
# методы keys(), values(), items()
print(my_dict.keys(), my_dict_2.values(), my_dict_2.items())
# методы словарей
# возвр. знач. ключа, но если его нет - возвращает default (по умолчанию None)
print(dict_1.get('job'))
# удаляет элемент по указ. ключу и возвращает его значени
name = info .pop('name')
print(info, name)
# возвр. знач. ключа, если его нет- создает ключ с указ. значением
info_2.setdefault('job', 'developer')
print(info_2)
info_2.update({'height': 180})  # позволяет обновить и дополнить словарь
print(info_2)
