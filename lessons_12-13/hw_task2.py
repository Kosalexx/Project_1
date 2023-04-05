from copy import deepcopy
from typing import Any, TypedDict


class BookTypes(TypedDict):
    Name: str
    Description: str
    Pages: int
    Author: str
    Price: float


class Book:
    def __init__(
            self,
            name: str,
            description: str,
            pages: int,
            author: str,
            price: float) -> None:
        self.name = name
        self.description = description
        self.pages = pages
        self.author = author
        self.price = price

    def to_dict(self) -> BookTypes:
        result: BookTypes = {
            "Name": self.name,
            "Description": self.description,
            "Pages": self.pages,
            "Author": self.author,
            "Price": self.price,
        }
        return result

    def contains_word(self, word: str) -> bool:
        return word in self.name

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return self.pages > other.pages

    def __ge__(self, other: Any) -> bool:
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return self.pages >= other.pages

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return ((self.pages == other.pages) and
                self.name == other.name and
                self.description == other.description and
                self.author == other.author and
                self.price == other.price)


class EmptyLibraryError(Exception):
    pass


class Library:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_books(self) -> list:
        return [obj.to_dict() for obj in self.books]

    def remove_book(self, book: Book) -> None:
        return self.books.remove(book)

    def find_the_biggest_book(self) -> BookTypes:
        if len(self.books) == 0:
            raise EmptyLibraryError("The Library is empty.")
        books_copy = deepcopy(self.books)
        books_copy.sort(key=lambda el: el.pages, reverse=True)
        result = books_copy[0].to_dict()
        return result

    def __len__(self) -> int:
        return len(self.books)


book1 = Book("1984", "Some description", 500, "Orwell", 10)
book2 = Book("Learn Python", "This book will teach you how to learn python",
             1000, "Luhts", 49)

print(book1.to_dict())
print(book1 == book2)

lib = Library()
lib.add_book(book1)
lib.add_book(book2)
print(lib.get_books())
print(lib.find_the_biggest_book())
print(len(lib))

lib.remove_book(book1)
print("After remove: ")
print(lib.get_books())
print(len(lib))
