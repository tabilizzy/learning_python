'''
Exercise file
'''
def greet():
    '''
A function to greet a user
'''
    name = input("Please enter your name: ")
    print(f"Hello {name}!, you are welcome")


greet()

#A loop printing numbers from 1–10

for i in range(1, 11):
    print(i)

# Another way of looping from 1-10
num = [1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)


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
    