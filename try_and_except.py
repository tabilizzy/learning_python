
# try:
#     num = int(input("enter a number: "))
#     print(num/0)
# except:
#     print("you can not divide by zero")

# def login():
#     try:
#         username = input("enter a username: ")
#         password = input("enter Password: ")
#         if username == "admin" and password == "1234":
#             print("Access granted")
#         else:
#             print("Access denied")
#     except:
#         print("something went wrong during login")

# login()

# try:
#     num = int(input("enter your age: "))
#     print(f"you are {num}")
# except:
#     print("please enter a number")

def get_number():
    try:
        num = int(input("enter a number: "))
        return num
    except ValueError:
        print("invaid input! please enter a number")
        return None

print(get_number())




