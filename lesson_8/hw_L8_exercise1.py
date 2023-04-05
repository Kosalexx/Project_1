b_string_1 = b'r\xc3\xa9sum\xc3\xa9'

string_1 = b_string_1.decode()
print(string_1)

byte_string_latin1 = string_1.encode('Latin1')
print(byte_string_latin1)

final_string = byte_string_latin1.decode('Latin1')
print(final_string)
