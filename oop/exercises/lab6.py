from abc import ABC, abstractmethod

class StudentManager(ABC):
    def add_student(self, student):
        pass

    def get_all_students(self):
        pass

    def find_student(self, name):
        pass

    def delete_student(self, name):
        pass

class Course:
    def __init__(self, grade, course_name ):
        self.course_name = course_name
        self.grade = grade

    def to_dict(self):
        return self.__dict__


class Student(StudentManager):
    def __init__(self, age: int, course, name = {}):
        self.name = name
        self.age = age
        self.course = course

    def add_student(self, student):
        self.name.add(student)
        
    def get_all_students(self):
        return f"{self.name}"

    def find_student(self, name):
        if name in self.name:
            print(name)

    def delete_student(self, name):
        if name in self.name:
            del name
            print("deleting was sucessful")

c1 = Course(100,"biology")
s = Student(17 ,c1, {"Lizzy"})
s.add_student("faith")
print(s.get_all_students())
s.find_student("faith")
s.add_student("faith")
s.add_student("faith")
print(s.get_all_students())

print(s.course.to_dict())


