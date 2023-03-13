from time import time
import re


class Censored:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        result = re.sub(r'[Ff][Uu][Cc][Kk]', '****', value)
        return setattr(instance, self.name, result)


class Message:
    text = Censored()

    def __init__(self, text) -> None:
        self.text = text
        self.created_at = time()


class Song:
    name = Censored()

    def __init__(self, name, author) -> None:
        self.name = name
        self.author = author
        self.created_at = time()


m1 = Message("Fuck sofof")
print(m1.text)

m2 = Message("Hello World")
print(m2.text)

m3 = Message("Fuck sofofucking sad")
print(m3.text)
