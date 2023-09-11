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
