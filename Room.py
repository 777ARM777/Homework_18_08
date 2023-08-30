class Room:
    def __init__(self, number: int, occupied: bool, capacity: int) -> None:
        if all([isinstance(i, int) for i in (number, capacity)]) and isinstance(occupied, bool):
            self.number = number
            self.occupied = occupied
            self.capacity = capacity

    def occupy_room(self) -> None:
        if not self.occupied:
            self.occupied = True
        else:
            raise ValueError("The room is already occupied")


class Course:
    def __init__(self, name: str, students_number: int) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Name must be string")
        if isinstance(students_number, int):
            self.students_number = students_number
        else:
            raise ValueError("Students number must be integer")

    def list_course_details(self) -> str:
        """Returns course details"""
        return f'Course: {self.name}.   Credits: {self.credit}.   Students: {self.students}'


try:
    room1 = Room(1, False, 10)
    room2 = Room(2, True, 20)
    course1 = Course('Python', 15)
    if not room1.occupied and room1.capacity >= course1.students_number:
        room1.occupy_room()
    elif not room2.occupied and room2.capacity >= course1.students_number:
        room2.occupy_room()
    else:
        print('There is no appropriate room to occupy')
    print(room1.occupied)
    print(room2.occupied)
except ValueError as ve:
    print(str(ve))
