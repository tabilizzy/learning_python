'''
Solution to assignment "warming up with Python"
'''
# 1.Write a program that adds 2 numbers and prints their sum.

x = 5
y = 7
add = x+y
print(add)

# 2.Write a function add_numbers(a, b). Return the sum and print the result.

def add_numbers(a,b):
    '''
    Adding two numbers and returning the sum
    '''
    
    return a+b


print(add_numbers(2, 5))

#3.Write a function that gets a number from a user and
#checks if the number is even or odd.

def check_num():
    '''
An if-statement checking if a number is odd or even
'''
    num = int(input("Please enter a number: "))
    if num%2 == 0:
        print(f"{num}! is even")
    else:
        print(f"{num}! is odd")


check_num()

#4.Create variables a, b, and operator. Use if/elif to perform addition,
#subtraction, multiplication, or division based on the operator and print the result.

a = 5
b = 6
ope = input("Please enter an operator: (+,-,*,/) ")
if ope == "+":
    result = a+b
    print(result)
elif ope == "-":
    result = a-b
    print(result)
elif ope == "*":
    result = a*b
    print(result)
elif ope == "/":
    result = a/b
    print(result)
else:
    print("you did not enter the right operator")

#5.Create a function greet(name). Print a greeting message using the name.
def greet():
    '''
A function to greet a user
'''
    name = input("Please enter your name: ")
    print(f"Hello {name}!, you are welcome")


greet()

#6.Write a program that checks if a person is a minor or an adult.
age = int(input("Please enter your age: "))
if age >= 18:
    print("You are an adult")
elif age >= 0:
    print("You are minor")
else:
    print("Hey your age can not be negative! ")

#7.Create a function square(x). Return the square of the number and print the result.
def square(x):
    '''
    calculating the square of a number
    '''
    return x*x


print(square(5))

#8.Write a program that checks two numbers and prints the one which is greater.
a = 5
b = 6
if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{b} is greater than {a}")
else:
    print("both numbers are equal")

#9.Simple Password Check: Store a password in a variable.
#Ask the user to input a password and check if it matches. Print access granted or denied.

PASSWORD = "Lizzy"
cpassword = input("Please enter your password: ")
if PASSWORD == cpassword:
    print("granted")
else:
    print("denied")

#10.Positive, Negative, or Zero: Create a variable num.
#Use if/elif/else to check whether it is positive, negative, or zero and print the result.
num = int(input("Please enter a number: "))
if num < 0:
    print(f"{num} is negative")
elif num > 0:
    print(f"{num} is positive")
else:
    print(f"{num} is zero")