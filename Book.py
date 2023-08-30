from collections.abc import Sequence


class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.libraries = []

    def add_to_library(self, library) -> None:
        """Adds book to the library"""
        library.add_book(self)
        self.libraries.append(library)

    def list_library_details(self) -> None:
        """Prints library details"""
        for library in self.libraries:
            print(library.name)

    def __str__(self) -> str:
        return f'{self.title} by {self.author}'


class Library:
    def __init__(self, name: str, book_list: (Sequence, Book)) -> None:
        self.name = name
        if isinstance(book_list, Book):
            self.book_list = book_list
        elif isinstance(book_list, Sequence) and all(isinstance(i, Book) for i in book_list):
            self.book_list = list(book_list)
        else:
            raise ValueError("Book list must be book type or sequence of books")

    def add_book(self, book: Book) -> None:
        """Adds book to the book list"""
        self.book_list.append(book)

    def remove_book(self, book: Book) -> None:
        """Removes book from book list"""
        self.book_list.remove(book)

    def __str__(self) -> str:
        return f'Library: {self.name}.\nBooks: {[book.__str__() for book in self.book_list]}'


book1 = Book('1st book', '1st author')
book2 = Book('2nd book', '2nd author')
book3 = Book('3rt book', '3th author')
book4 = Book('4rt book', '4th author')
try:
    library1 = Library('1st library', (book1, book2))
    print(book1)
    print(library1)
    library1.add_book(book3)
    library1.remove_book(book1)
    book4.add_to_library(library1)
    print(library1)
    book4.list_library_details()
except ValueError as ve:
    print(str(ve))
