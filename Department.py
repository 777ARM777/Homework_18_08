from collections.abc import Sequence


class Department:
    def __init__(self, name: str) -> None:
        self.name = name
        self.employees = []

    def add_employee(self, employees: (Sequence, str)) -> None:
        """Adds employee to the project"""
        if isinstance(employees, str):
            self.employees.append(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees.extend(employees)
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def list_department_details(self) -> str:
        """Returns department details"""
        return f'Department: {self.name}.\nEmployees: {self.employees}\n'


class Company:
    def __init__(self, name: str, departments: (Sequence, str), employees: (Sequence, str)) -> None:
        self.name = name
        if isinstance(departments, str):
            self.departments = departments
        elif isinstance(departments, Sequence) and all(isinstance(i, Department) for i in departments):
            self.departments = list(departments)
        else:
            raise ValueError("Departments must be string type or sequence of strings")

        if isinstance(employees, str):
            self.employees = employees
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees = list(employees)
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def add_department(self, department: Department) -> None:
        """Adds department to company"""
        self.department.append(department)

    def add_employees(self, department: Department, employees: (Sequence, str)) -> None:
        """Adds employees to department"""
        if isinstance(employees, str):
            self.departments[self.departments.index(department)].add_employee(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.departments[self.departments.index(department)].add_employee(list(employees))
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def __str__(self) -> str:
        s = f'Company: {self.name}.\n'
        for department in self.departments:
            s += department.list_department_details()
            s += '\n'
        return s


try:
    dep1 = Department('Python')
    dep2 = Department('Java')
    dep3 = Department('C++')
    cmp1 = Company('Picsart', (dep1, dep2, dep3), ('James', 'Bob', 'Adams'))
    cmp1.add_employees(dep1, ('James', 'Bob'))
    cmp1.add_employees(dep2, ('James', 'Bob', 'Adams'))
    cmp1.add_employees(dep3, ('Adams'))
    print(dep1.list_department_details())
    print(cmp1)
except ValueError as ve:
    print(str(ve))

