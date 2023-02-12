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
    # for key, value in dict_1.items():
    #     result_dict[key] = [value]
    #     if key not in dict_2:
    #         result_dict[key].append(None)
    # for key, value in dict_2.items():
    #     result_dict[key] = result_dict.setdefault(key, [None])
    #     result_dict[key].append(value)
    # return result_dict
    keys_set = set(list(dict_1.keys()) + list(dict_2.keys()))
    for key in keys_set:
        value1 = dict_1.get(key)
        value2 = dict_2.get(key)
        result_dict[key] = [value1]
        result_dict[key].append(value2)
    return result_dict


first_dict = {'a': 1, 'b': 2, 'c': 3}
second_dict = {'c': 3, 'd': 4, 'e': 5}
print(merge_dict(first_dict, second_dict))
