# making lab 6 interactive
# building and interactive student management system

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
    def __init__(self, age: int, course , name):
        self.name = name
        self.age = age
        self.course = course

    def create_student(self):
        student = input("Enter the Student name: ")
        age = int(input("Enter the student's age: "))
        course = input("Enter the students course: ")
        new_student = []
        self.name = new_student.append(student)
        return f"student was created"
        
    def get_all_students(self):
        return f"{self.name}"

    def find_student(self):
        name = input("enter the name you which to find: ")
        if name in self.name:
            print(name)

    def delete_student(self):
        name = input("enter the name you which to delete: ")
        if name in self.name:
            del name
            print("deleting was sucessful")

s = Student(14, "biology", "lizzy")

print("****************************************")
print("Welcome to Our Student Management System ")
print("****************************************")

choice = input("Do you wish to start (yes/no): ").lower()

while choice == "yes":
    print("\nSelect from Menu")
    print("""
    1. Create a student
    2. See all created students
    3. Find a student
    4. Delete a student
    5. Quit
    """)
    
        
    selection = input("\nEnter your choice (1-5): ")

    match selection:
        case "1":
            print("--- Creating a student ---")
            print(s.create_student())
            print()
        case "2":
            print("--- Displaying all students ---")
            print(s.get_all_students())
            print()
        case "3":
            print("--- Searching for a student ---")
            s.find_student()
            print()
        case "4":
            print("--- Deleting a student ---")
            s.delete_student()
            print()
        case "5":
            choice = "no"
            print("Thank you for your time. Goodbye!")
        case _:
            print("Invalid selection. Please pick a number between 1 and 5.")





