import json

my_dict = {}
my_dict[111111] = ('Sam', 30)
my_dict[222043] = ('Adam', 24)
my_dict[679432] = ('Jasy', 27)
my_dict[220004] = ('Vlad', 25)
my_dict[123040] = ('Alex', 19)
my_dict[633676] = ('Alexey', 28)
print(my_dict)

with open("data_file_ex3.json", "w") as write_file:
    json.dump(my_dict, write_file)
