class Publication:
    def __init__(self, title: str, price: float) -> None:
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError("The title must be string")
        if isinstance(price, (float, int)):
            self.price = float(price)
        else:
            raise ValueError("The price must be float")

    def get_publication(self, title: str, price: float) -> None:
        if isinstance(title, str):
            self.title = title
        else:
            raise ValueError("The title must be string")
        if isinstance(price, (float, int)):
            self.price = float(price)
        else:
            raise ValueError("The price must be float")

    def put_publication(self) -> tuple:
        return self.title, self.price


class Book(Publication):
    def __init__(self, title: str, price: float, page_count: int) -> None:
        if isinstance(title, str) and isinstance(price, (float, int)):
            super().__init__(title, price)
        else:
            raise ValueError("The title must be string and the price must be float")
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            raise ValueError("Page count must be integer")

    def get_book(self, title: str, price: float, page_count: int) -> None:
        if isinstance(title, str) and isinstance(price, (float, int)):
            super().get_publication(title, price)
        else:
            raise ValueError("The title must be string and the price must be float")
        if isinstance(page_count, int):
            self.page_count = page_count
        else:
            raise ValueError("Page count must be integer")

    def put_book(self) -> tuple:
        return self.title, self.price, self.page_count


class Tape(Publication):
    def __init__(self, title: str, price: float, time: float) -> None:
        if isinstance(title, str) and isinstance(price, (float, int)):
            super().__init__(title, price)
        else:
            raise ValueError("The title must be string and the price must be float")
        if isinstance(time, (float, int)):
            self.time = float(time)
        else:
            raise ValueError("Time must be float")

    def get_tape(self, title: str, price: float, time: float) -> None:
        if isinstance(title, str) and isinstance(price, (float, int)):
            super().get_publication(title, price)
        else:
            raise ValueError("The title must be string and the price must be float")
        if isinstance(time, (float, int)):
            self.time = float(time)
        else:
            raise ValueError("Time must be float")
        if isinstance(time, (float, int)):
            self.time = float(time)
        else:
            raise ValueError("Time must be float")

    def put_tape(self) -> tuple:
        return self.title, self.price, self.time


def main():
    try:
        book1 = Book('Python book', 15.5, 100)
        book2 = Book('Java book', 30, 200)
        tape1 = Tape('Python book', 15.5, 150)
        tape2 = Tape('Java book', 30, 300)
        book1.get_book('Python book', 20, 150)
        tape1.get_tape('Python book', 20, 250)
        print(book1.put_book())
        print(book2.put_book())
        print(tape1.put_tape())
        print(tape2.put_tape())
    except ValueError as ve:
        print(str(ve))


if __name__ == "__main__":
    main()
