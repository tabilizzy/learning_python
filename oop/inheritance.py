class Person:
    def speak(self):
        return "speaking...."

    def to_dict(self):
        return self.__dict__

class User(Person):
    def login(self):
        return "logging in ..."
# method overriding
    def speak(self):
        return "User speaking"

#multiple inheritance
class A:
    pass

class B:
    pass

class C(A, B):
    pass

print(C.__mro__)

user1 = User()

print(user1.login())
print(user1.speak())
print(user1.to_dict())

