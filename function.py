# def greet(name):
#     print(f"Hello {name}, You are Welcome")


# greet("Sir Boni")

# def add(a, b):
#     return a + b

# result = add(3,5)
# print(result)

# def greet(name = "Sir Boni"):
#     print(f"Hello {name}")


# greet()

# def claculations(a, b):
#     return a + b, a * b


# sum_result, product = claculations(2, 6)
# print(sum_result, product)

# def total(*numbers):
#     return sum(numbers)


# print(total(1,3,4,56,7))

# def info(**data):
#     print(data)


# info(name = "sam", age=21, status = "single")

# def login():
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     if username == "admin" and password == "1234":
#         return "Access granted"
#     else:
#         return "Access denied"

# print(login())

# def login():
#     attempts = 0
#     while attempts < 3:
#         username = input("Enter username: ")
#         password = input("Enter password: ")

#         if username == "admin" and password == "1234":
#             return "Access granted"
#         else:
#             print("Wrong Credentials")
#             attempts += 1
#     return "Account locked"

# print(login())

# def greet():
#     print("welcome to python programming")


# greet()

# def greet(name):
#     print(f"Hello {name}")

# greet("Sam")

# def sqr(num):
#     return num * num

# print(sqr(3))

# def sum(num1, num2):
#     return num1+ num2
    

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter number 2: "))
# result = sum(num1, num2)

# print(f"The sum of {num1} and {num2} is {result}")

# def max(num1, num2):
#     if num1 > num2:
#         return num1
#     else:
#         return num2

# print(max(6,17))

# def calculator():
#     num1 = int(input("please enter a number: "))
#     num2 = int(input("PLease enter another number: "))
#     operator = input("please enter an operator: (+, -, *, /): ")

#     match operator:
#         case "+":
#             return num1 + num2
#         case "-":
#             return num1 - num2
#         case "*":
#             return num1 * num2
#         case "/":
#             if num2 == 0:
#                 print("you cannot divide by zero ")
#                 return 0
#             return num1 / num2
#         case _:
#                 print("you did not put the right operator")

# print(calculator())

# def names():
#     count = 0
#     while count > 5
#         name = input("enter some names")
#         student_names = []
#         student_names.append(name)


#     for i in name_of_people:
#         print(f"Hello, {i}")

# names()

# count = 0
# student_names = []
# while count < 3:
#     name = input("enter some names: ")
#     student_names.append(name)
#     count+=1
# print(student_names)

# def greet():
#     count = 0
#     student_names = []
#     while count < 3:
#         name = input("enter some names: ")
#         student_names.append(name)
#         count+=1
#     # print(student_names)

#     for names in student_names:
#         print(f"Hello, {names}")

# greet()

