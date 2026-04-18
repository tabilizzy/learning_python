from abc import ABC, abstractmethod

class StudentManager(ABC):
    @abstractmethod
    def add_student(self): pass
    @abstractmethod
    def get_all_students(self): pass

class Course:
    def __init__(self, course_name, grade):
        self.course_name = course_name
        self.grade = grade

    # This makes the course look nice when you print it
    def __repr__(self):
        return f"{self.course_name}: {self.grade}"

class StudentSystem(StudentManager):
    def __init__(self):
        # This acts as our "database"
        self.students = []



    def add_student(self):
        name = input("Enter the Student name: ")
        age = input("Enter the student's age: ")
        
        #  Ask how many courses
        num_courses = int(input(f"How many courses does {name} have? "))
        student_courses = []

        #  Loop through and create each course
        for i in range(num_courses):
            print(f"\nCourse #{i+1}:")
            c_name = input("  Enter course name: ")
            c_grade = input("  Enter grade: ")
            
            # Create a Course object and add it to the list
            new_course = Course(c_name, c_grade)
            student_courses.append(new_course)

        #Save everything together
        self.students.append({
            "name": name,
            "age": age,
            "courses": student_courses
        })
        return f"\nSuccess: {name} was created with {len(student_courses)} courses!"


        
    def get_all_students(self):
        if not self.students:
            return "No students found."
        return self.students

    def find_student(self):
        search_name = input("Enter the name you wish to find: ")
        for student in self.students:
            if student['name'].lower() == search_name.lower():
                return student
        return "Student not found."

    def delete_student(self):
        name = input("Enter the name you wish to delete: ")
        for student in self.students:
            if student['name'].lower() == name.lower():
                self.students.remove(student)
                return f"{name} deleted successfully."
        return "Student not found."

# Initialize the system
system = StudentSystem()

print("****************************************")
print("Welcome to Our Student Management System ")
print("****************************************")

choice = input("Do you wish to start (yes/no): ").lower()

while choice == "yes":
    print("\nSelect from Menu")
    print("1. Create\n2. See all\n3. Find\n4. Delete\n5. Quit")
    
    selection = input("\nEnter choice (1-5): ")

    match selection:
        case "1":
            print(system.add_student())
        case "2":
            print(system.get_all_students())
        case "3":
            print(system.find_student())
        case "4":
            print(system.delete_student())
        case "5":
            print("Thank you for your time. Goodbye!")
            choice = "no"
        case _:
            print("Invalid selection.")
