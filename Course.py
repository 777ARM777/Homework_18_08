from collections.abc import Sequence


class Course:
    def __init__(self, name: str, credit: int) -> None:
        self.name = name
        self.credit = credit
        self.students = []

    def add_student(self, student: str) -> None:
        """Adds student to course"""
        self.students.append(student)

    def list_course_details(self) -> str:
        """Returns course details"""
        return f'Course: {self.name}.   Credits: {self.credit}.   Students: {self.students}'


class Department:
    def __init__(self, name: str, courses: Sequence):
        self.name = name
        if isinstance(courses, Course):
            self.courses = courses
        elif isinstance(courses, Sequence) and all(isinstance(i, Course) for i in courses):
            self.courses = list(courses)
        else:
            raise ValueError("Course list must be course type or sequence of courses")

    def add_course(self, course: Course) -> None:
        """Adds course to the department"""
        self.courses.append(course)

    def remove_course(self, course: Course) -> None:
        """Removes course from the department"""
        self.courses.remove(course)

    def add_students(self, students: Sequence, course: Course) -> None:
        """Adds students to the course"""
        if isinstance(courses, Course):
            self.courses[self.courses.index(course)].append(students)
        elif isinstance(courses, Sequence) and all(isinstance(i, Course) for i in courses):
            self.courses[self.courses.index(course)].extend(list(students))
        else:
            raise ValueError("Course list must be course type or sequence of courses")

    def __str__(self) -> str:
        return f'Department: {self.name}.   Courses: {[course.list_course_details() for course in self.courses]}'


course1 = Course('Python', 1000)
course2 = Course('Java', 2000)
course3 = Course('C++', 3000)
student1 = 'Bob'
student2 = 'James'
student3 = 'Adams'
course1.add_student(student1)
course1.add_student(student2)
course2.add_student(student1)
print(course1.list_course_details())
print(course1.list_course_details())
print(course1.list_course_details())

dep1 = Department('Picsart', (course1, course2))
print(dep1)
