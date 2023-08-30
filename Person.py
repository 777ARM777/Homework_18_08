class Person:
    def __init__(self, name: str, age: int) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be string")
        if isinstance(age, int):
            self.age = age
        else:
            raise ValueError("Age must be integer")

    def set_name(self, name:str) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be string")

    def set_age(self, age: int) -> None:
        if isinstance(age, int):
            self.age = age
        else:
            ValueError('Age must be integer')

    def print_Person(self) -> None:
        print(f'Name: {self.name}, age: {self.age}')


class Employee(Person):
    def __init__(self, name: str, age: int, id: int, department: int) -> None:
        if isinstance(name, str) and isinstance(age, int):
            super().__init__(name, age)
        else:
            raise ValueError("Name must be string and age must be integer")
        if isinstance(id, int):
            self.id = id
        else:
            raise ValueError("ID must be integer")
        if isinstance(department, int):
            self.department = department
        else:
            raise ValueError("Department must be integer")

    def set_id(self, id: int) -> None:
        if isinstance(id, int):
            self.id = id
        else:
            raise ValueError("ID must be integer")

    def set_department(self, department: int) -> None:
        if isinstance(department, int):
            self.department = department
        else:
            raise ValueError("Department must be integer")

    def print_Employee(self) -> None:
        print(f'Name: {self.name}\nAge: {self.age}\nID: {self.id}\nDepartment: {self.department}')

try:
    emp1 = Employee("Bob", 19, 1000, 15)
    emp2 = Employee("James", 10, 2000, 20)
    emp1.set_id(1001)
    emp2.set_age(15)
    emp2.set_department(8)
    emp1.set_name("Adams")
    emp1.print_Employee()
    emp2.print_Employee()
except ValueError as ve:
    print(str(ve))
