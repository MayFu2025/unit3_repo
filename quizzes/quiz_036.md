# Quiz 036
<hr>

### Prompt
![](images/quiz_036_slide.png)
*fig. 1* **Screenshot of quiz slides**

### Solution
UML Diagram:
![](images/quiz_036_diagram.png)
*fig. 2* **UML diagram for described classes**

Classes:
```.py
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Student(Person):
    def __init__(self, name, age, grade):
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
        self.students.remove(student)

    def class_average(self):
        sum = 0
        for student in self.students:
            sum += student.get_grade()
        return sum / len(self.students)
```

Testcase:
```.py
```

### Evidence
![](images/quiz_001_evidence.png)
*fig. 3* **Screenshot of output in console when running test file**