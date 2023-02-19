""" ЗАДАНИЕ 2
Есть 2 словаря
first_dict = { 'a': 1, 'b': 2, 'c': 3}
second_dict = { 'c': 3, 'd': 4,'e': 5}
Необходимо их объединить по ключам, а значения ключей поместить в список, если
у одного словаря есть ключ "а", а у другого нету, то поставить значение None на
соответствующую позицию(1-я позиция для 1-ого словаря, вторая для 2-ого)
merged_dict = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4],
'e': [None, 5]}
"""


def merge_dict(dict_1: dict, dict_2: dict) -> dict:
    """ Merges two dictionaries into one extended dictionary."""
    result_dict = {}
    keys_set = set(list(dict_1.keys()) + list(dict_2.keys()))
    for key in keys_set:
        result_dict[key] = [dict_1.get(key), dict_2.get(key)]
    return result_dict


first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}
print(merge_dict(first_dict, second_dict))
