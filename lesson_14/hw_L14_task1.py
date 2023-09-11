from typing import Self


class Alphabet:
    def __init__(self, end: str, lower: bool = True) -> None:
        self.lower = lower
        if self.lower:
            self.end = ord(end.lower())
        else:
            self.end = ord(end.upper())

    def __iter__(self) -> Self:
        if self.lower:
            self.first = ord('a')
        else:
            self.first = ord('A')
        self.ind_ascii = self.first
        return self

    def __next__(self) -> str:
        if self.ind_ascii >= self.end + 1:
            raise StopIteration
        result = chr(self.ind_ascii)
        self.ind_ascii += 1
        return result


alpha = Alphabet('H', lower=False)
for letter in alpha:
    print(letter)
