class Student:
    def __init__(self, name:str, grade:int):
        self.name = name
        if grade in range(1, 100):
            self.__grade = grade
        

    def get_grade(self):
        return self.__grade

    def set_grade(self, value:int):
        if value in range(1, 100):
            self.__grade
        else:
            raise ValueError("your grade is not in range or is not a whole number")


    def is_passing(self):
        if self.__grade >= 50:
            return f"your are passing"
        else:
            return f"you are failing"

s = Student("Marie", 75)
print(s.get_grade())
print(s.set_grade(95))
print(s.is_passing())
print(s.set_grade(150))
