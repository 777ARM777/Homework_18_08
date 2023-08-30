from Publication import Publication


class Date:
    def __init__(self, day: int, month: int, year: int):
        if (all([isinstance(i, int) for i in (day, month, year)])
                and 1 <= day <= 31 and 1 <= month <= 12 and 0 <= year <= 2023):
            self.day = day
            self.month = month
            self.year = year
        else:
            raise ValueError("Invalid date")


class Publication2(Publication):
    def __init__(self, title: str, price: float, date: Date) -> None:
        super().__init__(title, price)
        if isinstance(date, Date):
            self.date = date
        else:
            raise ValueError("The date must be of a type date")



class Book(Publication2):
    def __init__(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.page_count = input("Input the page count: ")
        d = int(input('Day: '))
        m = int(input('Month: '))
        y = int(input('Year: '))
        date = Date(d, m, y)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.page_count = int(self.page_count)
            super().__init__(title, price, date)
        except ValueError:
            print("The price must be float and page count must be integer")

    def get_book(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.page_count = input("Input the page count: ")
        d = int(input('Day: '))
        m = int(input('Month: '))
        y = int(input('Year: '))
        date = Date(d, m, y)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.page_count = int(self.page_count)
            super().__init__(title, price, date)
        except ValueError:
            print("The price must be float and page count must be integer")

    def put_book(self) -> tuple:
        return self.title, self.price, self.page_count

class Tape(Publication2):
    def __init__(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.time = input("Input the time: ")
        d = int(input('Day: '))
        m = int(input('Month: '))
        y = int(input('Year: '))
        date = Date(d, m, y)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.time = float(self.time)
            super().__init__(title, price, date)
        except ValueError:
            print("The price and the time must be float")

    def get_tape(self) -> None:
        title = input("Input the title: ")
        price = input("Input the price: ")
        self.time = input("Input the time: ")
        d = int(input('Day: '))
        m = int(input('Month: '))
        y = int(input('Year: '))
        date = Date(d, m, y)
        if not isinstance(date, Date):
            raise ValueError("The date must be of a type date")
        try:
            price = float(price)
            self.time = float(self.time)
            super().__init__(title, price, date)
        except ValueError:
            print("The price and the time must be float")

    def put_tape(self) -> tuple:
        return self.title, self.price, self.time


try:
    book1 = Book()
    tape1 = Tape()
    book1.get_book()
    tape1.get_tape()
    print(book1.put_book())
    print(tape1.put_tape())
except ValueError as ve:
    print(str(ve))
