from collections.abc import Sequence


class Project:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.employees = []

    def add_employee(self, employees: (Sequence, str)) -> None:
        """Adds employee to the project"""
        if isinstance(employees, str):
            self.employees.append(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees.extend(employees)
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def list_project_details(self) -> str:
        """Returns project details"""
        return f'Project: {self.name}.\n"""{self.description}""".\nEmployees: {self.employees}\n'

    def __str__(self):
        return self.list_project_details()


class Company:
    def __init__(self, name: str, projects: (Sequence, str), employees: (Sequence, str)) -> None:
        self.name = name
        if isinstance(projects, str):
            self.projects = projects
        elif isinstance(projects, Sequence) and all(isinstance(i, Project) for i in projects):
            self.projects = list(projects)
        else:
            raise ValueError("Projects must be string type or sequence of strings")

        if isinstance(employees, str):
            self.employees = employees
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.employees = list(employees)
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def add_project(self, project: Project) -> None:
        """Adds project to company"""
        self.projects.append(project)

    def add_employees(self, project: Project, employees: (Sequence, str)) -> None:
        """Adds employees to project"""
        if isinstance(employees, str):
            self.projects[self.projects.index(project)].add_employee(employees)
        elif isinstance(employees, Sequence) and all(isinstance(i, str) for i in employees):
            self.projects[self.projects.index(project)].add_employee(list(employees))
        else:
            raise ValueError("Employees must be string type or sequence of strings")

    def __str__(self) -> str:
        s = f'Company: {self.name}.\n'
        for project in self.projects:
            s += project.list_project_details()
            s += '\n'
        return s

try:
    proj1 = Project('Project1', '1st project')
    proj2 = Project('Project2', '2nd project')
    company1 = Company('Picsart', (proj1, proj2), ('Bob', 'James', 'Adams'))
    company1.add_employees(proj1, ('Bob', 'Adams'))
    company1.add_employees(proj2, ('James', 'Adams'))
    print(proj1)
    print(company1)
except ValueError as ve:
    print(str(ve))
