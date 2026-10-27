
class Student:
    def __init__(self, name: str, marks: list) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        average = sum(self.marks) / len(self.marks)
        return average > 50


student_1 = Student('Darek', [60, 75, 80])
student_2 = Student('Jarek', [30, 45, 50])

print(student_1.name, student_1.is_passed())
print(student_2.name, student_2.is_passed())
