""" Задание 1. Дан словарь, создать новый словарь, поменять
местами ключ и значение."""


def change_dict(dct: dict) -> dict:
    """Принимает в качестве аргумента словарь, возвращает новый
    словарь, в котором значения первого cловаря являются ключами,
    а ключи соответственно - значениями.
    """

    new_dict = {value: key for key, value in dct.items()}
    return new_dict


my_dict = {'name': 'Alexey', 'age': 28, 'group': 'Py35', 'English': 'A2'}
my_dict_2 = change_dict(my_dict)
print(my_dict)
print(my_dict_2)
