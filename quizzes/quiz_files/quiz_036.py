class Person():
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name:str, age:int, grade:int):
        super(Student, self).__init__(name, age)
        self.grade = grade

    def get_grade(self):
        return self.grade


# HL
class Classroom():
    def __init__(self):
        self.students = []

    def add_student(self, student:Student):
        self.students.append(student)

    def remove_student(self, student:Student):
        if student not in self.students:
            raise ValueError("Student does not exist in the classroom")
        else:
            self.students.remove(student)

    def class_average(self):
        sum = 0
        while len(self.students) == 0:
            raise ValueError("Classroom is empty")
        for student in self.students:
            sum += student.get_grade()
        return sum / len(self.students)