from copy import deepcopy


class Book:
    def __init__(self, name, description, pages, author, price) -> None:
        self.name = name
        self.description = description
        self.pages = pages
        self.author = author
        self.price = price

    def to_dict(self):
        return {
            "Name": self.name,
            "Description": self.description,
            "Pages": self.pages,
            "Author": self.author,
            "Price": self.price,
        }

    def contains_word(self, word) -> bool:
        return word in self.name

    def __gt__(self, other) -> bool:
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return self.pages > other.pages

    def __ge__(self, other) -> bool:
        if not isinstance(other, Book):
            raise ValueError("The second object must be Book.")
        return self.pages >= other.pages

    def __eq__(self, other) -> bool:
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
        self.books = []

    def add_book(self, book) -> None:
        self.books.append(book)

    def get_books(self) -> list:
        return [obj.to_dict() for obj in self.books]

    def remove_book(self, book) -> None:
        return self.books.remove(book)

    def find_the_biggest_book(self) -> dict:
        if len(self.books) == 0:
            raise EmptyLibraryError("The Library is empty.")
        books_copy = deepcopy(self.books)
        books_copy.sort(key=lambda el: el.pages, reverse=True)
        return books_copy[0].to_dict()

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
